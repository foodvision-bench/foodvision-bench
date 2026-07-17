# Test sets

Each test set has a fixed name, a fixed size, and a documented source of
ground truth. Adding a test set means adding a new `TestSet` entry in
`src/foodvision_bench/data/test_sets.py` and a new section here.

## `mini-215` (active primary set)

- **Size:** 215 images.
- **Ground truth:** USDA FoodData Central, per-ingredient lookup, weighed
  on an ISO-certified kitchen scale.
- **Coverage:** 40 food categories across five cuisine buckets — Western
  (62), East Asian (41), Mediterranean (35), South Asian (18), Latin
  American (17). Extends `mini-180` with the South Asian and Latin
  American buckets (added 2026-05, closing the original Western skew only
  partially — Western is still the largest bucket, and the two smallest
  buckets have N<20, so per-cuisine numbers carry wide confidence
  intervals; see `docs/methodology.md`).
- **License:** CC-BY 4.0 for the images; ground-truth kcal is derived
  from the USDA public-domain database.

This is the default test set and the set behind every number in the
current (2026-07) leaderboard.

## `mini-180` (predecessor, retired as primary)

- **Size:** 180 images.
- **Ground truth:** USDA FoodData Central, per-ingredient lookup, weighed
  on an ISO-certified kitchen scale.
- **Coverage:** 40 food categories. Western-skewed.
- **License:** CC-BY 4.0 for the images; ground-truth kcal is derived
  from the USDA public-domain database.

This was the primary set through the 2026-04 snapshot. It was superseded
by `mini-215` in 2026-05 but remains registered so the historical
snapshots (2025-11 .. 2026-04) that used it stay resolvable. New results
should use `mini-215`.

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
