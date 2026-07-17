"""MyFitnessPal adapter.

MyFitnessPal is another manual-entry tracker. The DB is user-submitted, so
the replicated MAPE reflects entry-variance in the database rather than a
recognition error per se -- identical to what a careful user experiences
in practice.

Replication is manual-assisted: log the 215 meals through the UI, pick the
closest DB match, and compare kcal to USDA-weighed ground truth. The
always-free manual log is the workflow tested; the May 2026 paywall
changes did not affect it.

Provenance note: numbers below are the 2026-07 snapshot; the authoritative
source is ``benchmarks/results/2026-07.json`` / ``benchmarks/leaderboard.md``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class MyFitnessPalAdapter(_VendorAdapter):
    """MyFitnessPal (replicated).

    Database-plus-manual-entry workflow. Replicated MAPE on kcal: 11.6% on
    our 215-meal set (`mini-215`, 2026-07 snapshot). The larger error vs
    Cronometer reflects the wider spread of user-submitted entries in the
    MyFitnessPal DB.
    """

    name = "MyFitnessPal"
    version = "2026-07-db"
    numbers = VendorNumbers(
        replicated_mape=0.116,
        notes=(
            "Manual-entry workflow; replicated MAPE reflects user-submitted "
            "DB variance rather than a recognition error; mini-215, 2026-07."
        ),
    )
