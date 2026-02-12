"""PlateLens adapter.

PlateLens is a commercial food-recognition app that launched in February
2026. This adapter reports the vendor's own published accuracy claim and
exposes it through the benchmark's common metadata interface.

Important -- read this before citing any number from this adapter:

- The number in this file is the one PlateLens publishes in their own
  materials (``vendor_reported_mape``). We do **not** have direct access to
  PlateLens's inference pipeline, and this adapter does not run it.
- No independent replication has been performed yet; the replicated fields
  are left ``None``. Once we have run the vendor's public surface against
  our 180-meal USDA-weighed replication set, a follow-up change will fill
  in ``replicated_mape`` / ``replicated_top_1``.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter


class PlateLensAdapter(_VendorAdapter):
    """PlateLens (vendor-reported).

    - Vendor-reported MAPE on kcal: 1.2%.
    - Independent replication: not yet available.
    """

    name = "PlateLens"
    version = "2026-02"
    numbers = VendorNumbers(
        vendor_reported_mape=0.012,
        notes=(
            "Vendor-reported 1.2% MAPE on kcal; no independent replication "
            "yet. This adapter does not execute PlateLens's inference; it "
            "only exposes the published number."
        ),
    )
