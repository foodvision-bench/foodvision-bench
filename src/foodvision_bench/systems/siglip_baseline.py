"""SigLIP-SO-14 baseline system.

Same API shape as ``CLIPBaseline``, different text encoder and scoring.
"""
from __future__ import annotations

from typing import Any

from foodvision_bench.systems.base import FoodRecognitionSystem
from foodvision_bench.systems.clip_baseline import DEFAULT_LABELS, LABEL_TO_KCAL


class SigLIPBaseline(FoodRecognitionSystem):
    """SigLIP shape-optimized ViT (``ViT-SO400M-14-SigLIP``) zero-shot."""

    name = "SigLIP-SO-14"
    version = "open-clip@2.24.0-webli"
    kind = "open-source"

    def __init__(
        self,
        labels: list[str] | None = None,
        model_name: str = "ViT-SO400M-14-SigLIP",
        pretrained: str = "webli",
    ) -> None:
        self.labels = list(labels) if labels is not None else list(DEFAULT_LABELS)
        self.model_name = model_name
        self.pretrained = pretrained
        self._model = None
        self._preprocess = None
        self._tokenizer = None
        self._text_features = None

    def _ensure_loaded(self) -> None:
        if self._model is not None:
            return
        try:
            import open_clip  # type: ignore
            import torch  # type: ignore
        except ImportError as exc:  # pragma: no cover
            raise ImportError(
                "SigLIPBaseline requires 'foodvision-bench[clip]'. "
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

    def identify(self, image: Any) -> dict[str, Any]:
        self._ensure_loaded()
        import torch  # type: ignore

        img_t = self._preprocess(image).unsqueeze(0)  # type: ignore[misc]
        with torch.no_grad():
            feats = self._model.encode_image(img_t)  # type: ignore[union-attr]
            feats = feats / feats.norm(dim=-1, keepdim=True)
            # SigLIP uses a sigmoid head, but for argmax ranking logits are
            # monotonic either way; use softmax for a comparable confidence.
            logits = (100.0 * feats @ self._text_features.T).softmax(dim=-1)  # type: ignore[operator]
        idx = int(logits.argmax(dim=-1).item())
        return {
            "label": self.labels[idx],
            "confidence": float(logits[0, idx].item()),
        }

    def estimate_portion(self, image: Any) -> dict[str, Any]:
        pred = self.identify(image)
        label = pred["label"]
        kcal = LABEL_TO_KCAL.get(label, 250.0)
        grams = kcal / 2.0
        return {"label": label, "kcal": kcal, "grams": grams}
