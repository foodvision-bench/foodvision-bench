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
