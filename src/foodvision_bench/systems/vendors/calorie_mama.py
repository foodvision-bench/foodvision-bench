"""Calorie Mama adapter.

Calorie Mama is a photo-based food-recognition product. We ran the public
app against the 231-meal USDA-weighed replication set (`mini-231`); the
``replicated_mape`` field reflects that measurement. The vendor-reported
claim (10.1% MAPE, taken from the product page) is retained for reference
but is not used for ranking -- it is the current live example of a
vendor-reported number diverging from an independent replication.

Provenance note: numbers below are the 2026-08 snapshot; the
authoritative source is ``benchmarks/results/2026-08.json`` /
``benchmarks/leaderboard.md``. Commercial-app replications are
manual-assisted and version-dependent, not bit-reproducible.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class CalorieMamaAdapter(_VendorAdapter):
    """Calorie Mama (replicated).

    Photo-based recognition. Replicated MAPE on kcal: 8.8% on our 231-meal
    USDA-weighed set (`mini-231`, 2026-08 snapshot). The vendor-reported
    claim of 10.1% is left in place for provenance but the leaderboard
    ranks on the replicated number.
    """

    name = "Calorie Mama"
    version = "2026-08-app"
    numbers = VendorNumbers(
        vendor_reported_mape=0.101,
        replicated_mape=0.088,
        replicated_top_1=0.640,
        notes=(
            "Black-box comparison against public app output on mini-231 "
            "(231-meal) set, 2026-08 snapshot; vendor-reported 10.1% "
            "retained for provenance."
        ),
    )
