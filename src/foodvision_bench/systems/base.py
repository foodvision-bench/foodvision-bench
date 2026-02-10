"""Abstract base class for food-recognition systems.

A system has two jobs from the benchmark's point of view:

1. ``identify(image)`` returns a dict with at least ``label``.
2. ``estimate_portion(image)`` returns a dict with at least ``kcal``.

Splitting them lets adapters share an identification backbone while varying
the portion-estimation strategy, which is how most real systems are built.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class FoodRecognitionSystem(ABC):
    """Common interface every benchmarked system implements."""

    #: Human-readable system name, e.g. "CLIP-ViT-L/14".
    name: str = "unnamed-system"

    #: Version string. For open-source models this is typically the model
    #: revision; for vendor adapters it is the date of the published number.
    version: str = "0.0.0"

    #: One of ``"open-source"`` or ``"vendor"``. Used for leaderboard sorting
    #: and for deciding whether numbers are independently reproducible.
    kind: str = "open-source"

    @abstractmethod
    def identify(self, image: Any) -> dict[str, Any]:
        """Return ``{"label": str, "confidence": float}`` (at minimum)."""

    @abstractmethod
    def estimate_portion(self, image: Any) -> dict[str, Any]:
        """Return ``{"kcal": float, "grams": float}`` (at minimum)."""

    # -- Convenience ---------------------------------------------------------

    def metadata(self) -> dict[str, Any]:
        """Static metadata for leaderboards / results files."""
        return {
            "name": self.name,
            "version": self.version,
            "kind": self.kind,
        }

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"<{type(self).__name__} name={self.name!r} version={self.version!r}>"
