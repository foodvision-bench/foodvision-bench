"""MacroFactor adapter.

MacroFactor is a manual-entry tracker. Included in the comparator set for
the same reason as Cronometer: it's a careful database-driven workflow,
so it's a useful baseline against photo-based image recognition.

Replicated through the app UI against the 180-meal USDA-weighed set.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class MacroFactorAdapter(_VendorAdapter):
    """MacroFactor (replicated).

    Database-plus-manual-entry workflow. Replicated MAPE on kcal: 4.8% on
    our 180-meal set, which is the second-lowest in the leaderboard among
    the replicated numbers at time of writing.
    """

    name = "MacroFactor"
    version = "2026-03-db"
    numbers = VendorNumbers(
        replicated_mape=0.048,
        notes="Manual-entry workflow; replicated MAPE on 180-meal set.",
    )
