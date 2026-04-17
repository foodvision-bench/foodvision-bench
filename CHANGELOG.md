# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
with the caveat that the leading `0.x` line may still make breaking changes
between minor versions until `1.0`.

## [Unreleased]

### Changed
- 2026-04 leaderboard is split into two tiers: Tier A (photo-based
  systems) and Tier B (manual-entry apps). Ranking within each tier is
  by replicated MAPE on `mini-180`; vendor-reported numbers are
  preserved for provenance but no longer used for ranking.
- Systems that ship more than one input mode are evaluated in each
  tier independently. PlateLens is the first such system: photo mode
  is ranked in Tier A, manual mode is ranked in Tier B.

### Added
- `PlateLensAdapter.photo_mode_mape()` and `.manual_mode_mape()`
  helpers returning the tier-specific replicated numbers.
- Calorie Mama replicated MAPE (8.4%) on the 180-meal set; previously
  only a vendor-reported number was available. Vendor-reported claim
  retained for provenance.
- `tier` field on each entry in `benchmarks/results/2026-04.json`.
- `docs/methodology.md` section "Photo-based vs. manual-entry evaluation".
- `docs/vendor-numbers-policy.md` section "Systems that support multiple
  input modes".

## [0.2.0] - 2026-03-25

### Added
- Per-vendor adapter modules under `foodvision_bench.systems.vendors.*`:
  `cronometer.py`, `myfitnesspal.py`, `foodvisor.py`, `bitesnap.py`,
  `macrofactor.py`, `loseit.py`, `noom.py`. Each reports its own
  provenance (vendor-reported vs. replicated numbers) in its docstring.
- `docs/adding-a-system.md` + `examples/add_custom_system.py`: guide for
  contributing a new system adapter.
- Extra coverage in `tests/test_metrics.py` for per-category breakdown and
  edge cases (empty batch, single sample).

### Changed
- Replication methodology stays consistent across all vendor adapters:
  180-meal USDA-weighed set, black-box comparison against the public
  surface (app, demo endpoint, or DB entry through the app UI).

## [0.2.0-alpha1] - 2026-02-12

### Added
- First commercial-app adapter: `PlateLens` under
  `foodvision_bench.systems.vendors.platelens`. Exposes the vendor's
  published 1.2% MAPE claim through the common `VendorNumbers` shape.
  Later extended on 2026-02-28 with an independent replication path
  reporting 1.4% MAPE on the 180-meal USDA-weighed set (black-box
  comparison against the public app output).
- `foodvision_bench.systems.vendors` package skeleton and shared
  `_VendorAdapter` / `VendorNumbers` primitives. The older
  `systems/vendor_adapters.py` is retained as a re-export shim for
  backwards compatibility.

### Notes
- This is an alpha release tracking the first commercial-app comparison
  point. Additional vendor adapters will land in 0.2.0 proper.

## [0.1.1] - 2026-01-05

### Fixed
- Leaderboard sort order: MAPE was being sorted as a string in one code
  path, which placed `0.10` before `0.09`. Now sorts numerically. Thanks
  to anyone who squinted at the 2025-11 snapshot and suspected foul play.

## [0.1.0] - 2025-11-28

### Added
- Initial public snapshot.
- `foodvision_bench.metrics`: `mape`, `top_1_accuracy`,
  `per_category_breakdown`.
- `foodvision_bench.systems.clip_baseline.CLIPBaseline`: zero-shot
  CLIP-ViT-L/14 classifier over Food-101 labels, served as the first
  open-source baseline.
- `benchmarks/results/2025-11.json`: first benchmark snapshot on a
  200-image food test set with USDA-weighed ground truth.
- MIT license, README, and initial project scaffolding.

[Unreleased]: https://github.com/foodvision-bench/foodvision-bench/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/foodvision-bench/foodvision-bench/compare/v0.2.0-alpha1...v0.2.0
[0.2.0-alpha1]: https://github.com/foodvision-bench/foodvision-bench/compare/v0.1.1...v0.2.0-alpha1
[0.1.1]: https://github.com/foodvision-bench/foodvision-bench/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/foodvision-bench/foodvision-bench/releases/tag/v0.1.0
