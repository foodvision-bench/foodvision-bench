# Methodology

This document explains how numbers in `benchmarks/results/*.json` and the
leaderboard are produced. The short version: one metric, one test set per
run, one commit SHA per result. Everything else is bookkeeping.

## Metrics

The primary metric is **MAPE (Mean Absolute Percent Error) on estimated
kilocalories**, reported as a fraction in [0, 1]. A result of 0.014
means the system is, on average, off by 1.4% of the true kcal value.

For image-recognition systems we also report **top-1 category accuracy**
against the test set's ground-truth label. Systems that are
database-plus-manual-entry (Cronometer, MyFitnessPal, MacroFactor,
Noom) do not have a top-1 accuracy in the conventional sense; those
entries are reported as `null`.

`per_category_breakdown` groups MAPE by ground-truth label so that a
system that happens to be strong on "pizza" but weak on "sushi" cannot
hide behind an overall average. The leaderboard reports the aggregate
number for brevity; consult the results JSON for the per-category view.

## Test sets

The primary test set is `mini-180`, a 180-meal set of real plates weighed
on an ISO-certified kitchen scale, with ground-truth kcal derived from
USDA FoodData Central lookups per weighed ingredient. The set is
deliberately small so that a replication run can be completed manually
inside a single afternoon.

Secondary test sets are registered under `src/foodvision_bench/data/test_sets.py`
and documented in `docs/test-sets.md`.

## Running a benchmark

```bash
pip install 'foodvision-bench[clip]'
foodvision-bench evaluate --system clip-vit-l --test-set mini-180
```

For commercial adapters without a live endpoint, `evaluate` reports the
static metadata (vendor-reported + replicated numbers). To reproduce a
replication run, a human has to actually submit each image through the
vendor's public surface and record the kcal estimate. The raw replication
logs for each result file live in `benchmarks/results/<date>-raw/`
when available.

## Error bars

- Vendor-reported numbers carry no measurement error from our side. They
  are what the vendor chose to publish.
- Replicated numbers carry the measurement error of our 180-meal set.
  Bootstrap 95% CIs are included in the per-run JSON under
  `mape_kcal_ci95`.
- Open-source baselines are rerun on every point release against the
  same 180-meal set; their numbers will drift as the upstream model
  weights drift, which is expected and noted in the changelog.

## Caveats

- `mini-180` is biased toward Western cuisine. We plan to expand with
  UEC-FOOD-256 and regional cuisine splits; see the open issues.
- Commercial apps update their databases and models continuously, so a
  replicated number is a snapshot, not a perpetual truth.
- Kcal is not the only dimension that matters. Macro-level error
  (protein / fat / carbs) and micronutrient error are out of scope for
  this repo at the moment.

## Ethics

We do not include any image in the test set that identifies a person or
a private location. All ground-truth labels were produced by the repo
contributors or taken from datasets with compatible licenses.

## Reproducibility checklist for a PR that changes a number

- [ ] The commit SHA of the code that produced the number is recorded in
      the results JSON under `commit`.
- [ ] The exact CLI invocation is in the PR description.
- [ ] The environment (OS, Python version, GPU) is in the PR description.
- [ ] For vendor replications: the date of the replication is in the
      results JSON, along with the app version when determinable.
