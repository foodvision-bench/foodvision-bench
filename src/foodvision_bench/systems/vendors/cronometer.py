"""Cronometer adapter.

Cronometer is a manual-entry calorie/macro tracker -- no image recognition
at all. It's included in the benchmark as a baseline for what a careful
database-driven workflow looks like compared to image-based estimation.

Because the surface is a manual form, replication is mechanical: log the
same 180 meals through their UI picking the closest database entry, and
compare the resulting kcal figures against the USDA-weighed ground truth.

- ``replicated_mape`` of 6.8% assumes a knowledgeable user picking the
  correct DB entry; a lazy or less-informed user will do worse.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class CronometerAdapter(_VendorAdapter):
    """Cronometer (replicated).

    Database-plus-manual-entry workflow; no image recognition. Replicated
    MAPE on kcal: 6.8% on our 180-meal set, assuming a knowledgeable user
    picking the correct DB entry.
    """

    name = "Cronometer"
    version = "2026-02-db"
    numbers = VendorNumbers(
        replicated_mape=0.068,
        notes="Manual-entry workflow; replicated MAPE assumes correct DB selection.",
    )
