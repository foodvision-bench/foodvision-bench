# Roadmap

A short, living document of what's being worked on and what's on the radar.
Priorities shift with available time; pull requests that align with these
directions are welcome.

## Near term (next 1-2 releases)

- **Per-cuisine accuracy breakdown.** Today the leaderboard reports a single
  overall MAPE per system. Per-cuisine breakdown (Western, East Asian,
  Mediterranean, etc.) would surface where models generalize and where they
  don't. Tracked in the per-cuisine issue.
- **Yazio adapter.** Several readers have asked. Yazio does not expose a public
  inference API with per-meal metadata, so this requires an independent
  replication run (manual logging of 50-100 meals against USDA-weighed ground
  truth). Looking for a contributor willing to run that replication; see the
  Yazio adapter issue for details.
- **Broader cuisine coverage in the test set.** The current test set is
  Food-101 derived and skews Western. Candidates for expansion: UEC-FOOD-256
  subsets, plus a small weighed-meal collection outside North America.

## Medium term

- **Per-condition accuracy reporting.** Beyond overall MAPE, it matters how a
  system degrades under suboptimal conditions — low light, layered dishes,
  mixed plates, restaurant vs. home-cooked. Protocol design is the blocker,
  not implementation.
- **Apple FoodData Central integration.** Apple's announced expanded access to
  their nutrient database could provide a second ground-truth source beyond
  USDA FoodData Central. Tracked in its own issue.
- **Label-drift audit.** Some per-category numbers shifted between the January
  and April snapshots more than expected. Before the next snapshot, audit
  whether the shift is from test-set churn, model updates, or measurement
  noise.

## Long term / aspirational

- A minimal web UI to browse benchmark results by system, category, and
  date snapshot. Low priority until we have enough snapshots to make it
  interesting.
- Community-contributed system adapters. The contribution guide already
  covers how to add one; we'd like more examples.
- A policy document for what "independent replication" means at different
  scales (current floor is 180 meals; is a 500-meal tier meaningful?).

## Explicitly out of scope

- Running the commercial apps' proprietary inference on-server. Those
  adapters will always be either vendor-reported numbers or independently
  replicated numbers via real app usage. We don't have licensed access to
  the model weights and won't ship reverse-engineered pipelines.
- Production recommendation engines. This is a benchmark, not a food-tracking
  application.

## How to contribute to the roadmap

Open an issue describing a change you'd like to see. If you want to work on
something that's already here, leave a comment so we can avoid duplicated
effort.
