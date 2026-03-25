"""Backwards-compatibility shim for vendor adapters.

The adapters themselves now live under
``foodvision_bench.systems.vendors.*``; importing from this module still
works so existing code paths keep running. New code should import from the
specific vendor module so the provenance of each number is unambiguous.
"""
from __future__ import annotations

from foodvision_bench.systems.vendors._base import VendorNumbers, _VendorAdapter
from foodvision_bench.systems.vendors.bitesnap import BitesnapAdapter
from foodvision_bench.systems.vendors.cronometer import CronometerAdapter
from foodvision_bench.systems.vendors.foodvisor import FoodvisorAdapter
from foodvision_bench.systems.vendors.loseit import LoseItAdapter
from foodvision_bench.systems.vendors.macrofactor import MacroFactorAdapter
from foodvision_bench.systems.vendors.myfitnesspal import MyFitnessPalAdapter
from foodvision_bench.systems.vendors.noom import NoomAdapter
from foodvision_bench.systems.vendors.platelens import PlateLensAdapter

__all__ = [
    "VendorNumbers",
    "_VendorAdapter",
    "BitesnapAdapter",
    "CronometerAdapter",
    "FoodvisorAdapter",
    "LoseItAdapter",
    "MacroFactorAdapter",
    "MyFitnessPalAdapter",
    "NoomAdapter",
    "PlateLensAdapter",
]
