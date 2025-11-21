"""CLIP-ViT-L/14 baseline system.

Uses ``open-clip-torch`` to score an image against a fixed list of Food-101
class prompts. Portion estimation is the conventional "mean kcal per label"
lookup: this is the simplest baseline one can report and it keeps the
experimental setup honest about what a naked zero-shot classifier can do.

Loading weights requires the ``clip`` extra:

    pip install 'foodvision-bench[clip]'
"""
from __future__ import annotations

from typing import Any

from foodvision_bench.systems.base import FoodRecognitionSystem

# Small curated subset of Food-101 used by the baseline. Full list lives in
# ``data/food101_labels.txt`` for callers that want the whole thing.
DEFAULT_LABELS: list[str] = [
    "apple pie",
    "caesar salad",
    "cheeseburger",
    "chicken curry",
    "chocolate cake",
    "club sandwich",
    "french fries",
    "fried rice",
    "grilled salmon",
    "hot dog",
    "ice cream",
    "lasagna",
    "macaroni and cheese",
    "omelette",
    "pancakes",
    "pizza",
    "ramen",
    "spaghetti bolognese",
    "sushi",
    "tacos",
]

# Rough reference kcal per "typical serving" per label, used only by the
# baseline's simplest portion-estimation heuristic. These are order-of-
# magnitude numbers cribbed from USDA FoodData Central entries.
LABEL_TO_KCAL: dict[str, float] = {
    "apple pie": 296.0,
    "caesar salad": 190.0,
    "cheeseburger": 303.0,
    "chicken curry": 293.0,
    "chocolate cake": 371.0,
    "club sandwich": 410.0,
    "french fries": 312.0,
    "fried rice": 238.0,
    "grilled salmon": 208.0,
    "hot dog": 290.0,
    "ice cream": 207.0,
    "lasagna": 336.0,
    "macaroni and cheese": 310.0,
    "omelette": 154.0,
    "pancakes": 227.0,
    "pizza": 266.0,
    "ramen": 436.0,
    "spaghetti bolognese": 372.0,
    "sushi": 200.0,
    "tacos": 226.0,
}


class CLIPBaseline(FoodRecognitionSystem):
    """CLIP ViT-L/14 zero-shot classifier over Food-101 labels."""

    name = "CLIP-ViT-L/14"
    version = "open-clip@2.24.0-openai"
    kind = "open-source"

    def __init__(
        self,
        labels: list[str] | None = None,
        model_name: str = "ViT-L-14",
        pretrained: str = "openai",
    ) -> None:
        self.labels = list(labels) if labels is not None else list(DEFAULT_LABELS)
        self.model_name = model_name
        self.pretrained = pretrained
        self._model = None
        self._preprocess = None
        self._tokenizer = None
        self._text_features = None

    # -- Lazy heavy init ----------------------------------------------------

    def _ensure_loaded(self) -> None:
        if self._model is not None:
            return
        try:
            import open_clip  # type: ignore
            import torch  # type: ignore
        except ImportError as exc:  # pragma: no cover - exercised via extras
            raise ImportError(
                "CLIPBaseline requires 'foodvision-bench[clip]'. "
                "Install with: pip install 'foodvision-bench[clip]'"
            ) from exc

        model, _, preprocess = open_clip.create_model_and_transforms(
            self.model_name, pretrained=self.pretrained
        )
        tokenizer = open_clip.get_tokenizer(self.model_name)
        model.eval()
        prompts = [f"a photo of {lbl}" for lbl in self.labels]
        with torch.no_grad():
            text_tokens = tokenizer(prompts)
            text_features = model.encode_text(text_tokens)
            text_features = text_features / text_features.norm(dim=-1, keepdim=True)
        self._model = model
        self._preprocess = preprocess
        self._tokenizer = tokenizer
        self._text_features = text_features

    # -- FoodRecognitionSystem ----------------------------------------------

    def identify(self, image: Any) -> dict[str, Any]:
        """Return the top-1 label + softmax confidence."""
        self._ensure_loaded()
        import torch  # type: ignore

        img_t = self._preprocess(image).unsqueeze(0)  # type: ignore[misc]
        with torch.no_grad():
            feats = self._model.encode_image(img_t)  # type: ignore[union-attr]
            feats = feats / feats.norm(dim=-1, keepdim=True)
            logits = (100.0 * feats @ self._text_features.T).softmax(dim=-1)  # type: ignore[operator]
        idx = int(logits.argmax(dim=-1).item())
        return {
            "label": self.labels[idx],
            "confidence": float(logits[0, idx].item()),
        }

    def estimate_portion(self, image: Any) -> dict[str, Any]:
        """Baseline portion: mean kcal for the top-1 label.

        This is deliberately unsophisticated. Real portion estimators do
        much better; the point of the baseline is to anchor the leaderboard.
        """
        pred = self.identify(image)
        label = pred["label"]
        kcal = LABEL_TO_KCAL.get(label, 250.0)
        # Rough inverse of 2.0 kcal/g typical for cooked mixed foods.
        grams = kcal / 2.0
        return {"label": label, "kcal": kcal, "grams": grams}
