# Roadmap

A short, living document of what's being worked on and what's on the radar.
Priorities shift with available time; pull requests that align with these
directions are welcome.

## Shipped recently

- **Per-cuisine accuracy breakdown.** *Shipped (2026-04, expanded 2026-05).*
  The leaderboard now reports per-cuisine MAPE for Tier A across five
  buckets. Note the small per-bucket N (17-62) — the breakdown is
  directional for the small buckets, not definitive; see
  `docs/methodology.md`.
- **First cuisine-coverage expansion.** *Shipped (2026-05).* `mini-180`
  became `mini-215` with South Asian (N=18) and Latin American (N=17)
  buckets. This reduced but did not remove the Western skew.

## Near term (next 1-2 releases)

- **Middle Eastern and Sub-Saharan African buckets.** The next test-set
  expansion. Contributor weighed-meal batches are being collected but are
  still under N=12 each, too small to publish. Targeted for 2026-Q3.
- **Yazio adapter.** Several readers have asked. Yazio does not expose a public
  inference API with per-meal metadata, so this requires an independent
  replication run (manual logging of 50-100 meals against USDA-weighed ground
  truth). Looking for a contributor willing to run that replication; see the
  Yazio adapter issue for details.
- **Larger overall N.** 215 meals separates systems that differ by whole
  points but is too small to certify production accuracy. Growing the set
  toward a 500-meal tier is tracked under the long-term item below.

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
