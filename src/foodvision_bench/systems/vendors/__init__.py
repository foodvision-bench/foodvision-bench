"""Per-vendor adapter modules.

Each commercial food-tracking system gets its own module here so that the
adapter code, vendor-reported numbers, and any independent-replication
numbers stay co-located and easy to audit.

The older ``foodvision_bench.systems.vendor_adapters`` module re-exports
everything defined here; new code should prefer importing from the specific
vendor module so the provenance of the numbers is unambiguous.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter

__all__ = ["VendorNumbers", "_VendorAdapter"]
