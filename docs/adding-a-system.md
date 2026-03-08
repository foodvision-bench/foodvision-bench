# Adding a new system

A "system" is anything you can point at a food image and get a kcal
estimate (and, ideally, a category label) from. An open-source model, a
commercial API, a classical CV pipeline: it all lives behind the same
`FoodRecognitionSystem` interface.

## 1. Subclass `FoodRecognitionSystem`

```python
from foodvision_bench.systems.base import FoodRecognitionSystem


class MyCoolModel(FoodRecognitionSystem):
    name = "my-cool-model"
    version = "0.1.0"
    kind = "open-source"  # or "vendor"

    def identify(self, image):
        # return {"label": "...", "confidence": float}
        ...

    def estimate_portion(self, image):
        # return {"label": "...", "kcal": float, "grams": float}
        ...
```

`identify` and `estimate_portion` are separate so that an adapter can
share an identification backbone across portion-estimation strategies,
which is how most real systems are built.

For **open-source** systems, both methods must be runnable. For **vendor**
systems that do not expose a public inference endpoint with the metadata
we need, inherit from `_VendorAdapter` in
`src/foodvision_bench/systems/vendor_adapters.py` and populate
`VendorNumbers` with your vendor-reported and replicated MAPE / top-1
numbers. Make it clear in the docstring which is which.

## 2. Register the system

Add a loader + registry entry in `src/foodvision_bench/systems/__init__.py`:

```python
def _load_my_cool_model():
    from foodvision_bench.systems.my_cool_model import MyCoolModel
    return MyCoolModel()

REGISTRY["my-cool-model"] = {
    "kind": "open-source",
    "description": "My cool model.",
    "loader": _load_my_cool_model,
}
```

The registry uses lazy loaders so that `foodvision-bench list-systems`
works without requiring every backend's heavy dependencies.

## 3. Add tests

At minimum:

- The adapter can be instantiated.
- `metadata()` returns the expected fields.
- If open-source: `identify` and `estimate_portion` return dicts with
  the required keys. Use `unittest.mock` to stub out the heavy model so
  the test doesn't require GPU or network.

See `tests/test_systems.py` for existing patterns.

## 4. Run a benchmark and record the number

```bash
foodvision-bench evaluate --system my-cool-model --test-set mini-180
```

Add the result to the most recent `benchmarks/results/<date>.json` file,
or open a PR with a new dated file if the run is a snapshot.

## 5. Open a PR

Use the PR template. The reviewer will check that:

- `pytest` and `ruff check .` pass.
- The adapter docstring states whether numbers are vendor-reported or
  independently measured.
- The leaderboard edit is backed by a results JSON.
- Commit messages are clear.

That's it. Welcome aboard.
