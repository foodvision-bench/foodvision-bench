"""Noom adapter.

Noom is a food-log tracker (manual entry against their DB). Replicated
through the app UI against the 231-meal USDA-weighed set (`mini-231`); it
sits at the upper end of the manual-entry MAPE range, which is mostly DB
variance.

Provenance note: numbers below are the 2026-08 snapshot; the authoritative
source is ``benchmarks/results/2026-08.json`` / ``benchmarks/leaderboard.md``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class NoomAdapter(_VendorAdapter):
    """Noom (replicated).

    Food-log workflow. Replicated MAPE on kcal: 12.4% on our 231-meal set
    (`mini-231`, 2026-08 snapshot).
    """

    name = "Noom"
    version = "2026-08-db"
    numbers = VendorNumbers(
        replicated_mape=0.124,
        notes="Food-log workflow; replicated on mini-231 (231-meal) set, 2026-08 snapshot.",
    )
