"""Bitesnap adapter.

Bitesnap is a photo-based food-tracking app. We ran the public app
against our 231-meal USDA-weighed replication set (`mini-231`) and
recorded the result here; this adapter does not execute Bitesnap's
inference.

- ``replicated_mape`` of 8.5% reflects the full black-box comparison
  against the app output on the current snapshot.

Provenance note: the numbers below are the 2026-08 snapshot. The
authoritative source for the current snapshot is
``benchmarks/results/2026-08.json`` and ``benchmarks/leaderboard.md``;
this static value is synced to the latest snapshot and may lag between
a snapshot and the corresponding code sync. Commercial-app replications
are manual-assisted (a human submits each image and transcribes the
output), so they are version- and time-dependent, not bit-reproducible.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class BitesnapAdapter(_VendorAdapter):
    """Bitesnap (replicated).

    Photo-based recognition. Replicated MAPE on kcal: 8.5% on our 231-meal
    USDA-weighed set (`mini-231`, 2026-08 snapshot).
    """

    name = "Bitesnap"
    version = "2026-08-app"
    numbers = VendorNumbers(
        replicated_mape=0.085,
        replicated_top_1=0.668,
        notes="Black-box comparison against public app output; mini-231 (231-meal) set, 2026-08 snapshot.",
    )
