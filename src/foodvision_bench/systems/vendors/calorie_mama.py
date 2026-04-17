"""Calorie Mama adapter.

Calorie Mama is a photo-based food-recognition product. For the April
2026 snapshot we ran the public app against the 180-meal USDA-weighed
replication set; the ``replicated_mape`` field reflects that measurement.
The older vendor-reported claim (10.1% MAPE, taken from the product
page) is retained for reference but is not used for ranking.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class CalorieMamaAdapter(_VendorAdapter):
    """Calorie Mama (replicated).

    Photo-based recognition. Replicated MAPE on kcal: 8.4% on our 180-meal
    USDA-weighed set. The vendor-reported claim of 10.1% is left in place
    for provenance but the leaderboard ranks on the replicated number.
    """

    name = "Calorie Mama"
    version = "2026-04-app"
    numbers = VendorNumbers(
        vendor_reported_mape=0.101,
        replicated_mape=0.084,
        replicated_top_1=0.651,
        notes=(
            "Black-box comparison against public app output on 180-meal "
            "USDA-weighed set; vendor-reported 10.1% retained for provenance."
        ),
    )
