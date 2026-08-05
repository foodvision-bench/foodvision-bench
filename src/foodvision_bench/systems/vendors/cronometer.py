"""Cronometer adapter.

Cronometer is a manual-entry calorie/macro tracker -- no image recognition
at all. It's included in the benchmark as a baseline for what a careful
database-driven workflow looks like compared to image-based estimation.

Because the surface is a manual form, replication is mechanical but still
manual-assisted: log the same 231 meals through their UI picking the
closest database entry, and compare the resulting kcal figures against the
USDA-weighed ground truth.

- ``replicated_mape`` of 6.7% assumes a knowledgeable user picking the
  correct DB entry; a lazy or less-informed user will do worse.

Provenance note: numbers below are the 2026-08 snapshot; the authoritative
source is ``benchmarks/results/2026-08.json`` / ``benchmarks/leaderboard.md``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class CronometerAdapter(_VendorAdapter):
    """Cronometer (replicated).

    Database-plus-manual-entry workflow; no image recognition. Replicated
    MAPE on kcal: 6.7% on our 231-meal set (`mini-231`, 2026-08 snapshot),
    assuming a knowledgeable user picking the correct DB entry.
    """

    name = "Cronometer"
    version = "2026-08-db"
    numbers = VendorNumbers(
        replicated_mape=0.067,
        notes="Manual-entry workflow; replicated MAPE assumes correct DB selection; mini-231, 2026-08.",
    )
