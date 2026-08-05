"""MyFitnessPal adapter.

MyFitnessPal is another manual-entry tracker. The DB is user-submitted, so
the replicated MAPE reflects entry-variance in the database rather than a
recognition error per se -- identical to what a careful user experiences
in practice.

Replication is manual-assisted: log the 231 meals through the UI, pick the
closest DB match, and compare kcal to USDA-weighed ground truth. The
always-free manual log is the workflow tested; the May 2026 paywall
changes did not affect it.

Provenance note: numbers below are the 2026-08 snapshot; the authoritative
source is ``benchmarks/results/2026-08.json`` / ``benchmarks/leaderboard.md``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class MyFitnessPalAdapter(_VendorAdapter):
    """MyFitnessPal (replicated).

    Database-plus-manual-entry workflow. Replicated MAPE on kcal: 11.7% on
    our 231-meal set (`mini-231`, 2026-08 snapshot). The larger error vs
    Cronometer reflects the wider spread of user-submitted entries in the
    MyFitnessPal DB.
    """

    name = "MyFitnessPal"
    version = "2026-08-db"
    numbers = VendorNumbers(
        replicated_mape=0.117,
        notes=(
            "Manual-entry workflow; replicated MAPE reflects user-submitted "
            "DB variance rather than a recognition error; mini-231, 2026-08."
        ),
    )
