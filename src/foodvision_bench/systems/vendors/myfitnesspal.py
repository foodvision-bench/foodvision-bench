"""MyFitnessPal adapter.

MyFitnessPal is another manual-entry tracker. The DB is user-submitted, so
the replicated MAPE reflects entry-variance in the database rather than a
recognition error per se -- identical to what a careful user experiences
in practice.

We have access to the UX for both Cronometer and MyFitnessPal, so
replication is straightforward: log the 180 meals through the UI, pick
the closest DB match, and compare kcal to USDA-weighed ground truth.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class MyFitnessPalAdapter(_VendorAdapter):
    """MyFitnessPal (replicated).

    Database-plus-manual-entry workflow. Replicated MAPE on kcal: 11.2% on
    our 180-meal set. The larger error vs Cronometer reflects the wider
    spread of user-submitted entries in the MyFitnessPal DB.
    """

    name = "MyFitnessPal"
    version = "2026-02-db"
    numbers = VendorNumbers(
        replicated_mape=0.112,
        notes=(
            "Manual-entry workflow; replicated MAPE reflects user-submitted "
            "DB variance rather than a recognition error."
        ),
    )
