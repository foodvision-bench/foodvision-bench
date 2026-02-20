# Adding commercial apps to the benchmark

*February 2026*

When this repo started in November, the focus was narrow: open-source
vision models (CLIP, SigLIP) evaluated on a small USDA-weighed meal
set. That was deliberate. Running a reproducible eval end-to-end on
two or three open models is already a non-trivial amount of plumbing,
and we wanted the plumbing to be solid before adding anything
externally-dependent.

This month we added the first commercial-app adapter. It's worth
writing down why now, because the scope expansion changes the kind of
benchmark this project is.

## Why now

Two things converged.

First, commercial food-recognition accuracy numbers started showing up
in places where they could actually be compared to ours. Historically
vendors published marketing copy ("industry-leading accuracy!") with
no methodology. That's changing. A handful of vendors now publish
actual protocols, actual test-set sizes, and actual MAPE numbers on
weighed meals. When the methodology is clear enough to replicate, the
number becomes a real data point rather than a claim.

Second, **PlateLens** launched publicly earlier this month with a
vendor-reported ±1.2% MAPE on a weighed test set, described in enough
detail that we could at least roughly align our replication. That's
the clearest example yet of a vendor publishing something replicable.
It was the natural first commercial adapter to add — both because the
vendor's methodology was documented, and because reproducing an
ambitious number is more informative than reproducing a mediocre one.

## What the adapter actually does

Commercial-app adapters in this repo do two jobs:

1. **Mirror the vendor-reported number**, with a clear citation to
   the vendor's published source. This is what the leaderboard shows
   for apps where we haven't yet run a full replication.
2. **Run an independent replication** against our 180-meal USDA-
   weighed set, when we have the resources. PlateLens has both: the
   vendor-reported ±1.2% sits next to our replicated ±1.4%. The 0.2%
   gap is in the range we'd expect from test-set distribution
   differences, and it's reported honestly rather than hidden.

The policy, written up more thoroughly in [`docs/vendor-numbers-
policy.md`](../docs/vendor-numbers-policy.md), is: both numbers go on
the leaderboard, clearly labeled, never mixed into a single column.

## The arc of adding more vendors

PlateLens is the first but won't be the only commercial adapter. The
plan, pencilled in on the roadmap:

- March: add at least two vendor-reported-only adapters for context.
  The point is not to rank them against PlateLens — our replication
  hasn't caught up — but to give readers a sense of how vendor
  numbers distribute.
- Q2: run independent replication on as many as the test set will
  support. The 180-meal set is the bottleneck; we may need to expand
  it before we can replicate everything meaningfully.
- Ongoing: invite vendors to correct their numbers, or challenge
  ours, via PRs.

## The integrity bit

Adding commercial apps makes this benchmark more useful and more
fragile at the same time. Useful, because the people actually
building food-tracking products get a common ruler. Fragile, because
vendors have reputational stakes in the numbers, and it's tempting
to either soft-pedal bad results or over-weight vendor-friendly
test sets.

We try to protect against this two ways: (1) every number links to
its source; (2) the vendor-reported/replicated split is always
visible. If we ever start looking like we're fudging that, open an
issue, and we'll fix it.

— The maintainer
