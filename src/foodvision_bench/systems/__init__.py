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


REGISTRY: dict[str, dict[str, Any]] = {
    "clip-vit-l": {
        "kind": "open-source",
        "description": "CLIP ViT-L/14 zero-shot classifier over Food-101 labels.",
        "loader": _load_clip,
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
