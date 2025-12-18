# Test sets

Each test set has a fixed name, a fixed size, and a documented source of
ground truth. Adding a test set means adding a new `TestSet` entry in
`src/foodvision_bench/data/test_sets.py` and a new section here.

## `mini-180`

- **Size:** 180 images.
- **Ground truth:** USDA FoodData Central, per-ingredient lookup, weighed
  on an ISO-certified kitchen scale.
- **Coverage:** 40 food categories. Biased toward Western cuisine; see
  the open issues for planned expansions.
- **License:** CC-BY 4.0 for the images; ground-truth kcal is derived
  from the USDA public-domain database.

This is the default test set used by every number in the 2026-04
leaderboard.

## `food101-test-500`

- **Size:** 500 images (first 500 examples of the Food-101 test split).
- **Ground truth:** category label only; no kcal.
- **Source:** Hugging Face `food101` dataset.
- **Use:** For category-accuracy probes that don't need kcal. Useful
  when comparing an open-source backbone against CLIP in a controlled
  setting.

## `uec-food-256-val`

- **Size:** 256 images.
- **Ground truth:** UEC category label only; no kcal.
- **Source:** UEC-FOOD-256 public dataset.
- **Use:** Broader cuisine coverage (East-Asian) to smoke-test a system
  that was tuned on Western food.

## Adding a new test set

1. Prepare the images under a single directory, one subdirectory per
   label. Ground-truth kcal, if available, as a `kcal.txt` file per
   label with one float per line (same order as images).
2. Open an issue with the `add-test-set` label. Include the license,
   a short description, and a sample of the ground-truth file.
3. Once the set is approved, register it in
   `src/foodvision_bench/data/test_sets.py` and document it here.
