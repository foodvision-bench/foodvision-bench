"""Shared primitives for vendor adapters.

See the individual ``platelens.py`` / ``cronometer.py`` / ... modules for
the actual per-vendor numbers. This file only defines the data container
and the abstract adapter behaviour (which is deliberately a no-op for
``identify`` / ``estimate_portion`` -- see the class docstrings for why).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from foodvision_bench.systems.base import FoodRecognitionSystem


@dataclass(frozen=True)
class VendorNumbers:
    """Numeric bundle for a vendor adapter's static metadata.

    Attributes
    ----------
    vendor_reported_mape:
        The MAPE on kcal the vendor has published in their own materials.
        Recorded verbatim; no editorial reinterpretation.
    replicated_mape:
        The MAPE we observed when running the vendor's public surface (app,
        demo endpoint, or cached output) against our 180-meal USDA-weighed
        replication set. ``None`` if we have not yet run a replication.
    replicated_top_1:
        Top-1 category accuracy observed during replication.
    replication_test_set:
        Short identifier for the test set used in the replication.
    notes:
        Free-form provenance note. Anything non-obvious about where the
        numbers came from or what they exclude should go here.
    """

    vendor_reported_mape: float | None = None
    replicated_mape: float | None = None
    replicated_top_1: float | None = None
    replication_test_set: str = "mini-180 (USDA-weighed)"
    notes: str = ""


class _VendorAdapter(FoodRecognitionSystem):
    """Shared implementation for vendor adapters.

    Vendor adapters do **not** run the vendor's inference pipeline locally.
    They expose the published or replicated numbers through ``metadata()``
    and raise a clear ``NotImplementedError`` from ``identify`` /
    ``estimate_portion``. The benchmark runner special-cases vendor kinds
    so that leaderboard rows can still be produced from the static numbers.

    Subclasses set ``name``, ``version``, and ``numbers``.
    """

    numbers: VendorNumbers = VendorNumbers()
    kind = "vendor"

    def identify(self, image: Any) -> dict[str, Any]:
        raise NotImplementedError(
            f"{self.name} does not expose a public inference endpoint with "
            "the metadata required to compute a fresh prediction. See the "
            "class docstring for the vendor-reported / replicated numbers."
        )

    def estimate_portion(self, image: Any) -> dict[str, Any]:
        raise NotImplementedError(
            f"{self.name} does not expose a public inference endpoint with "
            "the metadata required to compute a fresh portion estimate."
        )

    def metadata(self) -> dict[str, Any]:
        base = super().metadata()
        base.update(
            {
                "vendor_reported_mape": self.numbers.vendor_reported_mape,
                "replicated_mape": self.numbers.replicated_mape,
                "replicated_top_1": self.numbers.replicated_top_1,
                "replication_test_set": self.numbers.replication_test_set,
                "notes": self.numbers.notes,
            }
        )
        return base
