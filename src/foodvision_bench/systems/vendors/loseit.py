"""Lose It! adapter.

Lose It! offers both a database-entry workflow and a "Snap-It" image
recognition feature. For replication we used the primary manual / barcode
workflow as a typical user would; the Snap-It photo feature is secondary.

Provenance note: numbers below are the 2026-08 snapshot; the authoritative
source is ``benchmarks/results/2026-08.json`` / ``benchmarks/leaderboard.md``.
The replication is manual-assisted and version-dependent.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class LoseItAdapter(_VendorAdapter):
    """Lose It! (replicated).

    Primary manual / barcode workflow (Snap-It photo feature is secondary).
    Replicated MAPE on kcal: 9.6% on our 231-meal set (`mini-231`, 2026-08 snapshot).
    """

    name = "Lose It!"
    version = "2026-08-db"
    numbers = VendorNumbers(
        replicated_mape=0.096,
        notes="Primary manual / barcode workflow; replicated on mini-231 (231-meal) set, 2026-08.",
    )
