"""MacroFactor adapter.

MacroFactor is a manual-entry tracker. Included in the comparator set for
the same reason as Cronometer: it's a careful database-driven workflow,
so it's a useful baseline against photo-based image recognition.

Replicated through the app UI against the 231-meal USDA-weighed set
(`mini-231`).

Provenance note: numbers below are the 2026-08 snapshot; the authoritative
source is ``benchmarks/results/2026-08.json`` / ``benchmarks/leaderboard.md``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class MacroFactorAdapter(_VendorAdapter):
    """MacroFactor (replicated).

    Database-plus-manual-entry workflow. Replicated MAPE on kcal: 4.9% on
    our 231-meal set (`mini-231`, 2026-08 snapshot). This is the
    second-lowest replicated MAPE in Tier B, behind PlateLens (manual
    mode) at 3.3%.
    """

    name = "MacroFactor"
    version = "2026-08-db"
    numbers = VendorNumbers(
        replicated_mape=0.049,
        notes=(
            "Manual-entry workflow; replicated MAPE on mini-231 (231-meal) "
            "set, 2026-08 snapshot. Second in Tier B behind PlateLens "
            "(manual mode) at 3.3%."
        ),
    )
