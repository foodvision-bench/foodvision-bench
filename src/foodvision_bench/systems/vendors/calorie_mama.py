"""Calorie Mama adapter.

Calorie Mama is a photo-based food-recognition product. We do not
currently run an independent replication against our 180-meal set; the
number here is the vendor's published claim. Left clearly labelled so it
can't be confused with a replicated result.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class CalorieMamaAdapter(_VendorAdapter):
    """Calorie Mama (vendor-reported).

    No independent replication yet; the number is the vendor's published
    claim, recorded verbatim.
    """

    name = "Calorie Mama"
    version = "2026-01-vendor-page"
    numbers = VendorNumbers(
        vendor_reported_mape=0.101,
        replicated_top_1=0.651,
        notes="Vendor-reported; no independent replication yet.",
    )
