"""Foodvisor adapter.

Foodvisor is a photo-based food-recognition product with a public demo
endpoint. This is a more direct comparison point for PlateLens than the
manual-entry apps, since both consume an image and produce a
kcal/category prediction end-to-end.

- ``replicated_mape`` was measured by exercising the public demo endpoint
  on our 180-meal set where rate limits permitted (some meals required
  retrying across days).
- Vendor-reported MAPE is not published in a form directly comparable to
  our metric, so the field is left ``None``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class FoodvisorAdapter(_VendorAdapter):
    """Foodvisor (replicated via public demo).

    Photo-based recognition. Replicated MAPE on kcal: 5.1% on our 180-meal
    USDA-weighed set. Rate-limited; measurement took several days to
    collect across the full set.
    """

    name = "Foodvisor"
    version = "2026-02-demo"
    numbers = VendorNumbers(
        vendor_reported_mape=None,
        replicated_mape=0.051,
        replicated_top_1=0.762,
        notes="Exercised public demo endpoint; rate-limited.",
    )
