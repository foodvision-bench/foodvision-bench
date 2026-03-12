"""Bitesnap adapter.

Bitesnap is a photo-based food-tracking app. We ran the public app
against our 180-meal USDA-weighed replication set and recorded the
result here; this adapter does not execute Bitesnap's inference.

- ``replicated_mape`` of 7.9% reflects the full black-box comparison
  against the app output.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class BitesnapAdapter(_VendorAdapter):
    """Bitesnap (replicated).

    Photo-based recognition. Replicated MAPE on kcal: 7.9% on our 180-meal
    USDA-weighed set.
    """

    name = "Bitesnap"
    version = "2026-03-app"
    numbers = VendorNumbers(
        replicated_mape=0.079,
        replicated_top_1=0.684,
        notes="Black-box comparison against public app output; 180-meal set.",
    )
