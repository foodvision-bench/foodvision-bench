"""Registry of named test sets.

Keeps the CLI and docs honest: every named test set that appears in a
``benchmarks/results/*.json`` file should be resolvable from here.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TestSet:
    name: str
    n: int
    description: str
    ground_truth: str

    def as_dict(self) -> dict[str, str | int]:
        return {
            "name": self.name,
            "n": self.n,
            "description": self.description,
            "ground_truth": self.ground_truth,
        }


_REGISTRY: dict[str, TestSet] = {
    "mini-231": TestSet(
        name="mini-231",
        n=231,
        description=(
            "231 USDA-weighed meals spanning 40 food categories across six "
            "cuisine buckets (Western 62, East Asian 41, Mediterranean 35, "
            "South Asian 18, Latin American 17, Middle Eastern 16). Active "
            "primary set since the 2026-08 snapshot; extends mini-215."
        ),
        ground_truth="USDA FoodData Central lookup per weighed ingredient.",
    ),
    "mini-215": TestSet(
        name="mini-215",
        n=215,
        description=(
            "215 USDA-weighed meals spanning 40 food categories across five "
            "cuisine buckets (Western 62, East Asian 41, Mediterranean 35, "
            "South Asian 18, Latin American 17). Primary set for the 2026-05 .. "
            "2026-07 snapshots; superseded by mini-231 but kept registered so "
            "those snapshots stay resolvable."
        ),
        ground_truth="USDA FoodData Central lookup per weighed ingredient.",
    ),
    "mini-180": TestSet(
        name="mini-180",
        n=180,
        description=(
            "180 USDA-weighed meals spanning 40 food categories. Predecessor "
            "of mini-215; retired as the primary set in 2026-05 but kept "
            "registered so historical snapshots (2025-11 .. 2026-04) remain "
            "resolvable. Western-skewed."
        ),
        ground_truth="USDA FoodData Central lookup per weighed ingredient.",
    ),
    "food101-test-500": TestSet(
        name="food101-test-500",
        n=500,
        description="First 500 examples of the Hugging Face Food-101 test split.",
        ground_truth="Food-101 category label only (no kcal).",
    ),
    "uec-food-256-val": TestSet(
        name="uec-food-256-val",
        n=256,
        description="Held-out slice of UEC-FOOD-256, covering East-Asian cuisine.",
        ground_truth="UEC category label; no kcal.",
    ),
}


def list_test_sets() -> list[TestSet]:
    return sorted(_REGISTRY.values(), key=lambda t: t.name)


def resolve(name: str) -> TestSet:
    if name not in _REGISTRY:
        raise KeyError(f"unknown test set '{name}'. Known: {sorted(_REGISTRY)}")
    return _REGISTRY[name]
