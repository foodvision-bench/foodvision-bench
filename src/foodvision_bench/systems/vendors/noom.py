"""Noom adapter.

Noom is a food-log tracker (manual entry against their DB). Replicated
through the app UI against the 180-meal USDA-weighed set; it sits at the
upper end of the manual-entry MAPE range, which is mostly DB variance.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class NoomAdapter(_VendorAdapter):
    """Noom (replicated).

    Food-log workflow. Replicated MAPE on kcal: 12.3% on our 180-meal set.
    """

    name = "Noom"
    version = "2026-03-db"
    numbers = VendorNumbers(
        replicated_mape=0.123,
        notes="Food-log workflow; replicated on 180-meal set.",
    )
