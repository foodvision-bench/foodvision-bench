# Benchmarks

Each dated JSON under `results/` is a snapshot of the leaderboard at a
point in time. Snapshots are not retroactively edited; to correct a
number, add a new snapshot with a later date.

## Schema

```
{
  "date":         "YYYY-MM",
  "commit":       "<git sha of foodvision-bench at the time>",
  "test_set":     "mini-180",
  "environment":  { "python": "3.12.x", "os": "ubuntu-22.04", "gpu": "none" },
  "entries": [
    {
      "system":          "CLIP-ViT-L/14",
      "system_version":  "open-clip@2.24.0-openai",
      "kind":            "open-source",
      "mape_kcal":       0.091,
      "mape_kcal_ci95":  [0.082, 0.101],
      "top_1":           0.612,
      "source":          "open-source",
      "notes":           "independently measured"
    },
    ...
  ]
}
```

Numbers labelled `"source": "vendor-reported"` come from publicly-published
vendor benchmarks. Numbers labelled `"source": "replicated"` come from
the 180-meal USDA-weighed replication run described in
[`../docs/methodology.md`](../docs/methodology.md). Numbers labelled
`"source": "open-source"` are run directly by this package.

## Reproducing a run

1. Install the package:
   ```bash
   pip install 'foodvision-bench[clip]'
   ```
2. Point it at your local copy of `mini-180`:
   ```bash
   foodvision-bench evaluate --system clip-vit-l --test-set mini-180
   ```
3. Compare your output against the relevant `results/<date>.json`.

If the numbers disagree materially, open an issue with your environment
and raw output. See `CONTRIBUTING.md`.
