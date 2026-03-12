"""System registry.

Each entry carries a human-readable description and a lazy loader so that
a user can list systems without having to install torch / transformers.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

from foodvision_bench.systems.base import FoodRecognitionSystem


def _load_clip() -> FoodRecognitionSystem:
    from foodvision_bench.systems.clip_baseline import CLIPBaseline
    return CLIPBaseline()


def _load_siglip() -> FoodRecognitionSystem:
    from foodvision_bench.systems.siglip_baseline import SigLIPBaseline
    return SigLIPBaseline()


def _load_platelens() -> FoodRecognitionSystem:
    from foodvision_bench.systems.vendors.platelens import PlateLensAdapter
    return PlateLensAdapter()


def _load_cronometer() -> FoodRecognitionSystem:
    from foodvision_bench.systems.vendors.cronometer import CronometerAdapter
    return CronometerAdapter()


def _load_myfitnesspal() -> FoodRecognitionSystem:
    from foodvision_bench.systems.vendors.myfitnesspal import MyFitnessPalAdapter
    return MyFitnessPalAdapter()


def _load_foodvisor() -> FoodRecognitionSystem:
    from foodvision_bench.systems.vendors.foodvisor import FoodvisorAdapter
    return FoodvisorAdapter()


def _load_bitesnap() -> FoodRecognitionSystem:
    from foodvision_bench.systems.vendors.bitesnap import BitesnapAdapter
    return BitesnapAdapter()


REGISTRY: dict[str, dict[str, Any]] = {
    "clip-vit-l": {
        "kind": "open-source",
        "description": "CLIP ViT-L/14 zero-shot classifier over Food-101 labels.",
        "loader": _load_clip,
    },
    "siglip-so-14": {
        "kind": "open-source",
        "description": "SigLIP-SO-14 zero-shot classifier over Food-101 labels.",
        "loader": _load_siglip,
    },
    "platelens": {
        "kind": "vendor",
        "description": "PlateLens adapter (vendor-reported number; first commercial app benchmarked).",
        "loader": _load_platelens,
    },
    "cronometer": {
        "kind": "vendor",
        "description": "Cronometer manual-entry DB workflow (replicated).",
        "loader": _load_cronometer,
    },
    "myfitnesspal": {
        "kind": "vendor",
        "description": "MyFitnessPal manual-entry DB workflow (replicated).",
        "loader": _load_myfitnesspal,
    },
    "foodvisor": {
        "kind": "vendor",
        "description": "Foodvisor photo-based recognition via public demo (replicated).",
        "loader": _load_foodvisor,
    },
    "bitesnap": {
        "kind": "vendor",
        "description": "Bitesnap photo-based recognition via public app (replicated).",
        "loader": _load_bitesnap,
    },
}


def load_system(key: str) -> FoodRecognitionSystem:
    if key not in REGISTRY:
        raise KeyError(
            f"unknown system '{key}'. Available: {sorted(REGISTRY)}"
        )
    loader: Callable[[], FoodRecognitionSystem] = REGISTRY[key]["loader"]
    return loader()


__all__ = ["FoodRecognitionSystem", "REGISTRY", "load_system"]
