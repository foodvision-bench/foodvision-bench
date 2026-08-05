"""Foodvisor adapter.

Foodvisor is a photo-based food-recognition product with a public demo
endpoint. This is a more direct comparison point for PlateLens than the
manual-entry apps, since both consume an image and produce a
kcal/category prediction end-to-end.

- ``replicated_mape`` was measured by exercising the public demo endpoint
  on our 231-meal set (`mini-231`) where rate limits permitted (some meals
  required retrying across days). Across 2026-06, 2026-07 and 2026-08
  Foodvisor improved on the South Asian bucket in three consecutive
  snapshots. Note its 2026-08 aggregate rose (5.1% -> 5.3%) purely because
  the test set expanded to mini-231; measured against the fixed baselines'
  +0.4pp shift, it gained ground.
- Vendor-reported MAPE is not published in a form directly comparable to
  our metric, so the field is left ``None``.

Provenance note: numbers below are the 2026-08 snapshot; the authoritative
source is ``benchmarks/results/2026-08.json`` / ``benchmarks/leaderboard.md``.
The demo-endpoint replication is manual-assisted and time-dependent.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class FoodvisorAdapter(_VendorAdapter):
    """Foodvisor (replicated via public demo).

    Photo-based recognition. Replicated MAPE on kcal: 5.3% on our 231-meal
    USDA-weighed set (`mini-231`, 2026-08 snapshot). Rate-limited;
    measurement took several days to collect across the full set.
    """

    name = "Foodvisor"
    version = "2026-08-demo"
    numbers = VendorNumbers(
        vendor_reported_mape=None,
        replicated_mape=0.053,
        replicated_top_1=0.749,
        notes="Exercised public demo endpoint; rate-limited; mini-231, 2026-08 snapshot.",
    )
