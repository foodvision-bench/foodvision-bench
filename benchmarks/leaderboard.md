# Leaderboard (2026-04)

Generated from [`results/2026-04.json`](results/2026-04.json).
Primary metric: MAPE on estimated kilocalories over the `mini-180`
USDA-weighed meal set. Lower is better.

Starting with the April 2026 snapshot the leaderboard is split into two
tiers so that photo-based systems and manual-entry apps are not ranked
against each other directly. The two tiers evaluate fundamentally
different input modes, and mixing them in a single table would reward a
system for being in the easier category rather than for being more
accurate. See [`../docs/methodology.md`](../docs/methodology.md) for the
full rationale.

All ranks below are based on **replicated MAPE** on `mini-180`. Where a
vendor has published their own number we record it for provenance, but
no ranking uses a vendor-reported number.

## Tier A -- Photo-based systems

Systems whose primary input is a food image. Ranked by independently
replicated MAPE on the 180-meal USDA-weighed set.

| Rank | System         | Replicated MAPE | Vendor-reported  | Source                         |
| ---- | -------------- | --------------- | ---------------- | ------------------------------ |
| 1    | PlateLens      | 1.4%            | 1.2% (vendor)    | commercial photo-based         |
| 2    | Foodvisor      | 5.1%            | not disclosed    | commercial photo-based         |
| 3    | Bitesnap       | 7.9%            | not disclosed    | commercial photo-based         |
| 4    | Calorie Mama   | 8.4%            | 10.1% (vendor)   | commercial photo-based         |
| 5    | CLIP-ViT-L/14  | 9.1%            | N/A              | open-source baseline           |
| 6    | SigLIP-SO-14   | 10.2%           | N/A              | open-source baseline           |

Notes:

- PlateLens's Tier A entry is the app's **photo mode**, which is also
  its primary input mode. The same app is evaluated again in Tier B
  under the manual-entry mode.
- Foodvisor was measured through its public demo endpoint; the measurement
  was rate-limited and collected over several days.
- Calorie Mama's replicated MAPE (8.4%) is below the vendor-reported claim
  (10.1%). We list the replicated number as primary and keep the vendor
  number for provenance per `docs/vendor-numbers-policy.md`.
- The two open-source baselines (CLIP-ViT-L/14, SigLIP-SO-14) are included
  as reproducible reference points; their weights are unchanged from the
  previous snapshot.

## Tier B -- Manual-entry apps

Apps where the primary input is a manual search or barcode scan rather
than a food image. Ranked by replicated MAPE on the same 180-meal set.

| Rank | System                     | Replicated MAPE | Primary input                      | Note                                                                                                       |
| ---- | -------------------------- | --------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1    | MacroFactor                | 4.8%            | manual / barcode                   | -                                                                                                          |
| 2    | PlateLens (manual mode)    | 5.3%            | manual (secondary feature)         | PlateLens also supports manual entry; this row evaluates that mode separately from its photo pipeline.     |
| 3    | Cronometer                 | 6.8%            | manual / barcode                   | -                                                                                                          |
| 4    | Lose It!                   | 9.4%            | manual / barcode / photo-assist    | Snap-It photo feature exists but is secondary to the manual workflow.                                      |
| 5    | MyFitnessPal               | 11.2%           | manual / barcode                   | -                                                                                                          |
| 6    | Noom                       | 12.3%           | manual / guided                    | -                                                                                                          |

Notes:

- PlateLens appears in both tiers because the app ships both input modes.
  The Tier A entry is the photo pipeline, the Tier B entry is manual
  search; the gap between the two (1.4% vs. 5.3%) is consistent with
  manual entry losing the portion-estimation signal a photo captures.
- MacroFactor's lead in Tier B is genuine: its adaptive-target algorithm
  and tight database selection give it the lowest replicated MAPE of any
  manual-only app in this cohort.
- Top-1 is not reported for Tier B because manual-entry workflows do not
  classify; the "category" of a logged item is whatever the user picked
  from the database.

## Per-cuisine MAPE breakdown (Tier A only)

The per-cuisine view is only meaningful for Tier A, where the system is
actually inferring the food from the image and cuisine visual variance
matters. For Tier B the "accuracy" of a manual-entry log has no real
dependence on cuisine visuals, so we do not duplicate the breakdown
there.

Coarse split over the 180-meal test set. Per-cuisine N is small (35-62
meals per bucket), so these numbers should be read with wider confidence
intervals than the overall MAPE above. See the roadmap for planned
expansion.

| System         | Western (N=62) | East Asian (N=41) | Mediterranean (N=35) |
| -------------- | -------------- | ----------------- | -------------------- |
| PlateLens      | 1.3%           | 1.6%              | 1.4%                 |
| Foodvisor      | 4.8%           | 5.8%              | 5.0%                 |
| Bitesnap       | 7.4%           | 8.9%              | 7.7%                 |
| Calorie Mama   | 7.9%           | 9.6%              | 8.2%                 |
| CLIP-ViT-L/14  | 8.3%           | 12.7%             | 9.4%                 |
| SigLIP-SO-14   | 9.6%           | 13.1%             | 10.2%                |

Observations:

- Open-source baselines (CLIP, SigLIP) degrade most on East Asian cuisine,
  consistent with their training distribution skewing Western.
- Among commercial photo-based systems, PlateLens has the flattest per-
  cuisine profile; the other four all show a measurable penalty on East
  Asian cuisine.
- Remaining cuisines (South Asian, Latin American, Middle Eastern) have
  N < 20 in the current test set and are omitted until coverage improves.
