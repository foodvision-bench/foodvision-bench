"""Foodvisor adapter.

Foodvisor is a photo-based food-recognition product with a public demo
endpoint. This is a more direct comparison point for PlateLens than the
manual-entry apps, since both consume an image and produce a
kcal/category prediction end-to-end.

- ``replicated_mape`` was measured by exercising the public demo endpoint
  on our 215-meal set (`mini-215`) where rate limits permitted (some meals
  required retrying across days). Over 2026-06 and 2026-07 Foodvisor
  improved on the South Asian bucket specifically, which is where most of
  its recent overall improvement comes from.
- Vendor-reported MAPE is not published in a form directly comparable to
  our metric, so the field is left ``None``.

Provenance note: numbers below are the 2026-07 snapshot; the authoritative
source is ``benchmarks/results/2026-07.json`` / ``benchmarks/leaderboard.md``.
The demo-endpoint replication is manual-assisted and time-dependent.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class FoodvisorAdapter(_VendorAdapter):
    """Foodvisor (replicated via public demo).

    Photo-based recognition. Replicated MAPE on kcal: 5.1% on our 215-meal
    USDA-weighed set (`mini-215`, 2026-07 snapshot). Rate-limited;
    measurement took several days to collect across the full set.
    """

    name = "Foodvisor"
    version = "2026-07-demo"
    numbers = VendorNumbers(
        vendor_reported_mape=None,
        replicated_mape=0.051,
        replicated_top_1=0.753,
        notes="Exercised public demo endpoint; rate-limited; mini-215, 2026-07 snapshot.",
    )
