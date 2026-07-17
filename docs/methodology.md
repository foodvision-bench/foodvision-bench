# Methodology

This document explains how numbers in `benchmarks/results/*.json` and the
leaderboard are produced, and — just as importantly — what they do **not**
support. The short version: one metric, one test set per run, one commit
SHA per result. Everything else is bookkeeping, and the limitations at the
bottom are not boilerplate — read them before citing any number.

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

## Test set

The active primary test set is **`mini-215`**: 215 real plates weighed on
an ISO-certified kitchen scale, with ground-truth kcal derived from USDA
FoodData Central lookups per weighed ingredient. It spans 40 food
categories across five cuisine buckets:

| Bucket         | N  |
| -------------- | -- |
| Western        | 62 |
| East Asian     | 41 |
| Mediterranean  | 35 |
| South Asian    | 18 |
| Latin American | 17 |

`mini-215` was introduced in the **2026-05** snapshot; it extends the
earlier **`mini-180`** set with the South Asian and Latin American
buckets. `mini-180` is retired as the primary set but stays registered so
the historical snapshots that used it (2025-11 through 2026-04) remain
resolvable. Any snapshot's own JSON records which test set produced it.

The set is deliberately small so that a full replication run — which is
partly manual, see below — can be completed by hand. That is a real
constraint on what the numbers can claim; see **Limitations**.

Secondary test sets (`food101-test-500`, `uec-food-256-val`) are
registered under `src/foodvision_bench/data/test_sets.py` and documented
in `docs/test-sets.md`.

## Running a benchmark

```bash
pip install 'foodvision-bench[clip]'
foodvision-bench evaluate --system clip-vit-l --test-set mini-215
```

## Reproducibility tiers — read this before comparing numbers

Not every number on the leaderboard is reproducible in the same sense.
There are two distinct tiers, and conflating them is the most common way
to over-read the results:

1. **Bit-reproducible (open-source baselines: CLIP-ViT-L/14,
   SigLIP-SO-14).** These run locally through `open-clip` with fixed
   weights, a fixed 40-label prompt, and deterministic decoding on the
   fixed test set. Anyone who installs the package and runs the CLI gets
   the same number to the last digit. Because of this, we report them
   **bit-identical across snapshots** and use them as a *control*: if a
   snapshot's open-source numbers ever moved, it would mean the harness
   or the test set changed, not the systems.

2. **Manual-assisted replication (every commercial app: PlateLens,
   Foodvisor, Bitesnap, Calorie Mama, MacroFactor, Cronometer, Lose It!,
   MyFitnessPal, Noom).** These are **not** automated. We do not have the
   vendors' model weights or a metadata-complete API. A person submits
   each of the 215 images (or logs each meal) through the app or demo
   endpoint and transcribes the kcal the app reports. This means the
   number depends on:
   - the **app/model version** on the day of the run (vendors ship silent
     updates),
   - the **account/region** and any A/B bucket it lands in,
   - **human decisions** — which database entry a manual-entry app user
     picks, how a portion is confirmed — which we standardize with a
     protocol but cannot eliminate,
   - **demo-endpoint conditions** (rate limits, fallback categories).

   A commercial number is therefore a **snapshot of a moving target**, not
   a perpetual or bit-reproducible truth. We record the date, the app
   version when determinable, and the method in each result. Two people
   following the protocol should land close, but not identical.

`evaluate` for a commercial adapter reports the **static metadata**
(vendor-reported + latest replicated numbers) rather than executing a
run, precisely because the run is manual. The adapter docstrings and the
results JSON are the source of truth; the numbers hardcoded in adapters
are synced to the latest snapshot and may lag it by one commit.

## Photo-based vs. manual-entry evaluation

Starting with the April 2026 snapshot, the leaderboard is split into two
tiers so that systems with fundamentally different input modes are not
ranked against each other directly.

- **Tier A — Photo-based systems.** The system accepts a food image and
  returns a kcal estimate end-to-end. Included: PlateLens (photo mode),
  Foodvisor, Bitesnap, Calorie Mama, and the two open-source baselines
  CLIP-ViT-L/14 and SigLIP-SO-14. Per-cuisine breakdowns are reported for
  this tier.
- **Tier B — Manual-entry apps.** The primary input is a text search or
  barcode scan against an in-app food database; photo support, if
  present, is a secondary feature. Included: MacroFactor, PlateLens
  (manual mode), Cronometer, Lose It!, MyFitnessPal, Noom.

Why split:

1. *Fairness.* A manual-entry app ranks higher than a photo-based system
   if the user happens to pick the correct DB entry, which tells you
   about the user's discipline more than about the system. A photo-based
   system has to infer both the food and the portion. Ranking the two
   in a single table rewards systems for being in the easier category.
2. *Comparability.* Within a tier, the ranking is directly interpretable.
3. *Complete coverage.* An app that supports both input modes is
   evaluated in both tiers. PlateLens is the canonical example: its
   photo pipeline is benchmarked in Tier A and its manual-entry workflow
   in Tier B. The two measurements are produced on the same 215-meal set
   so the gap between them is interpretable as the cost of logging by
   hand instead of by camera.

Ranking rule: both tiers rank on **replicated MAPE**. Vendor-reported
numbers are recorded for provenance but never used for ranking, even
when they are the only published number the vendor has.

## Error bars

- Vendor-reported numbers carry no measurement error from our side. They
  are what the vendor chose to publish.
- Replicated numbers carry the measurement error of a 215-meal set.
  Bootstrap 95% CIs are included in the per-run JSON under
  `mape_kcal_ci95` where computed. On a set this size the overall CI is
  already non-trivial; the **per-cuisine** CIs are wide (see below).
- Open-source baselines are deterministic on the fixed set, so their only
  drift comes from an upstream weight change, which is noted in the
  changelog.

## Limitations

These are load-bearing. The leaderboard is a small, partly-manual
benchmark, and the numbers should be read accordingly.

- **Small overall N.** 215 meals is enough to separate systems that differ
  by whole percentage points (e.g. 1.1% vs 5.1%), but it is *not* enough
  to certify a system's "true" accuracy in production, across the full
  diversity of real meals, to the precision the decimals suggest. Read a
  0.1pp month-to-month move as noise, not signal.
- **Very small per-cuisine N.** The per-cuisine buckets range from 62
  (Western) down to **17 (Latin American)** and **18 (South Asian)**.
  Per-bucket differences should be read as **directional, not
  definitive** — an 18-meal bucket cannot support a confident ranking
  claim between two close systems. We publish the breakdown because the
  *large* gaps in it are informative, not because the small ones are
  precise.
- **Residual cuisine skew.** The set was originally Western-heavy. The
  2026-05 expansion (South Asian, Latin American) reduced but did not
  eliminate the skew; Western is still the largest bucket, and Middle
  Eastern and Sub-Saharan African cuisines are not yet represented at
  usable N. "Most accurate across every cuisine bucket measured" means
  *measured* — it is not a claim about cuisines we do not yet cover.
- **Commercial numbers are manual-assisted and version-dependent.** See
  the reproducibility tiers above. They can and do move when a vendor
  ships an update, and they carry human-in-the-loop variance.
- **Kcal only.** Macro-level error (protein / fat / carbs) and
  micronutrient error are out of scope. A system can be excellent on
  calories and mediocre on micros; this benchmark does not tell you.
- **Not a production guarantee.** A leaderboard MAPE is an estimate under
  a controlled protocol on a fixed set. It is a useful comparative
  signal, not a warranty of the accuracy any individual user will see on
  their own meals.

## Ethics

We do not include any image in the test set that identifies a person or
a private location. All ground-truth labels were produced by the repo
contributors or taken from datasets with compatible licenses.

## Reproducibility checklist for a PR that changes a number

- [ ] The commit SHA of the code that produced the number is recorded in
      the results JSON under `commit`.
- [ ] The exact CLI invocation is in the PR description.
- [ ] The environment (OS, Python version, GPU) is in the PR description.
- [ ] For commercial replications: the date of the replication is in the
      results JSON, along with the app version when determinable, and the
      run is labelled as manual-assisted (see reproducibility tiers).
