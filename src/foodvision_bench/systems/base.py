"""Abstract base class for food-recognition systems.

A system has two jobs from the benchmark's point of view: return a label
for an image, and return a kcal estimate for the same image. Splitting
them lets adapters share an identification backbone while varying the
portion-estimation strategy, which is how most real systems are built.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class FoodRecognitionSystem(ABC):
    """Common interface every benchmarked system implements."""

    name: str = "unnamed-system"
    version: str = "0.0.0"
    kind: str = "open-source"

    @abstractmethod
    def identify(self, image: Any) -> dict[str, Any]:
        """Return ``{"label": str, "confidence": float}`` (at minimum)."""

    @abstractmethod
    def estimate_portion(self, image: Any) -> dict[str, Any]:
        """Return ``{"kcal": float, "grams": float}`` (at minimum)."""
