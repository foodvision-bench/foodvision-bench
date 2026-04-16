# Interpreting MAPE

The leaderboard's primary metric is MAPE on kcal: the mean, across test
meals, of

```
|predicted_kcal - true_kcal| / true_kcal
```

expressed as a fraction (0.012 means 1.2%). If you're used to seeing an
absolute error in kcal, MAPE can feel unintuitive at first -- this page
tries to make it less so.

## What MAPE is

MAPE is a **relative** error: each meal's error is normalised by that
meal's true kcal. A 30 kcal miss on a 300 kcal salad (10% MAPE) is
treated the same as a 90 kcal miss on a 900 kcal pasta dish (10% MAPE).
The two are different absolute errors but similar "how wrong was the
system, proportionally."

## Why we use MAPE (and not just absolute kcal error)

A test set with a wide range of meal sizes -- everything from a 120 kcal
snack to a 1200 kcal dinner plate -- punishes models on the big meals if
you average absolute error. A system could score well by systematically
under-predicting large meals and still look bad in kcal terms. MAPE
normalises this out: a 10% error is a 10% error whether the meal is
small or large.

We still publish per-meal absolute errors in the JSON artefacts, and a
purely-absolute MAE is easy to compute from the same data if you prefer
it.

## How to read the per-category breakdown

Each benchmark snapshot in `benchmarks/results/<date>.json` has a
`per_category` field keyed by food label (e.g. `"pizza"`, `"ramen"`,
`"salad"`). For each category we report:

- `n`: number of meals in that category in the test set.
- `mape_kcal`: MAPE averaged over those meals only.
- `top_1`: fraction of those meals where the category was correctly
  identified before portion estimation.

A big per-category MAPE on a small `n` (say, ramen with `n=4`) is a
weaker signal than the same MAPE on `n=30`; treat per-category numbers
as directional rather than definitive.

## Caveats

- MAPE blows up when the true value is near zero. Our test meals all
  have `true_kcal > 50`, so this isn't a practical issue; if you extend
  the test set to diet sodas or plain water, switch to a symmetric
  variant (sMAPE) or a fixed-denominator error.
- MAPE penalises over-prediction more than under-prediction on small
  meals. That's a known property of the metric, not a bug.

## See also

- [`methodology.md`](methodology.md) for how the ground truth is built.
- [`test-sets.md`](test-sets.md) for what's in each test set.
