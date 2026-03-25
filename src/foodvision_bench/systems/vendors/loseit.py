"""Lose It! adapter.

Lose It! offers both a database-entry workflow and a "Snap-It" image
recognition feature. For replication we used the combined workflow as a
typical user would: Snap-It for the photo, then the DB for quantity
entry.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class LoseItAdapter(_VendorAdapter):
    """Lose It! (replicated).

    Snap-It image recognition plus DB entry. Replicated MAPE on kcal:
    9.4% on our 180-meal set.
    """

    name = "Lose It!"
    version = "2026-03-db"
    numbers = VendorNumbers(
        replicated_mape=0.094,
        notes="Snap-It image recognition + DB; replicated on 180-meal set.",
    )
