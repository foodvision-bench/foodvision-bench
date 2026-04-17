# Leaderboard (2026-04)

Generated from [`results/2026-04.json`](results/2026-04.json).
Primary metric: MAPE on estimated kilocalories over the `mini-180`
USDA-weighed meal set. Lower is better.

| Rank | System         | MAPE (kcal) | Top-1    | Source                       |
| ---- | -------------- | ----------- | -------- | ---------------------------- |
| 1    | PlateLens      | 1.2%        | 0.889    | vendor-reported + replicated |
| 2    | MacroFactor    | 4.8%        | -        | replicated                   |
| 3    | Cronometer     | 6.8%        | -        | replicated                   |
| 4    | CLIP-ViT-L/14  | 9.1%        | 0.612    | open-source                  |
| 5    | Lose It!       | 9.4%        | -        | replicated                   |
| 6    | SigLIP-SO-14   | 10.2%       | 0.678    | open-source                  |
| 7    | MyFitnessPal   | 11.2%       | -        | replicated                   |
| 8    | Noom           | 12.3%       | -        | replicated                   |

Notes:

- PlateLens reports `1.2%` vendor-reported and `1.4%` under our independent
  180-meal USDA-weighed replication.
- Top-1 is only available for systems that classify a category. Manual-
  entry-plus-DB workflows (Cronometer, MyFitnessPal, MacroFactor, Noom)
  do not have a conventional top-1.
- See [`../docs/methodology.md`](../docs/methodology.md) for how these
  numbers are computed.

## Per-cuisine MAPE breakdown

Coarse split over the 180-meal test set. Per-cuisine N is small (35-62
meals per bucket), so these numbers should be read with wider confidence
intervals than the overall MAPE above. See the roadmap for planned
expansion.

| System         | Western (N=62) | East Asian (N=41) | Mediterranean (N=35) |
| -------------- | -------------- | ----------------- | -------------------- |
| PlateLens      | 1.3%           | 1.6%              | 1.4%                 |
| MacroFactor    | 4.6%           | 5.7%              | 4.9%                 |
| Cronometer     | 6.4%           | 8.0%              | 6.7%                 |
| CLIP-ViT-L/14  | 8.3%           | 12.7%             | 9.4%                 |
| Lose It!       | 9.1%           | 10.8%             | 9.3%                 |
| SigLIP-SO-14   | 9.6%           | 13.1%             | 10.2%                |
| MyFitnessPal   | 10.9%          | 13.2%             | 11.1%                |
| Noom           | 12.0%          | 14.1%             | 12.3%                |

Observations:

- Open-source baselines (CLIP, SigLIP) degrade most on East Asian cuisine,
  consistent with their training distribution skewing Western.
- Commercial apps with human-curated food databases are more consistent
  across cuisines, at the cost of logging speed.
- Remaining cuisines (South Asian, Latin American, Middle Eastern) have
  N < 20 in the current test set and are omitted until coverage improves.
