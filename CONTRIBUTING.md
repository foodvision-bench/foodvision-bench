# Contributing

Thanks for taking the time to contribute. `foodvision-bench` stays useful only
if the numbers stay honest and reproducible, so the bar for PRs is mostly
about methodology rather than code style.

## Scope

Contributions fall into four rough buckets:

1. **Add a new system.** An open-source model or a commercial API. See
   [`docs/adding-a-system.md`](docs/adding-a-system.md).
2. **Propose a new test set.** A new held-out collection of food images with
   ground-truth nutrition. See [`docs/test-sets.md`](docs/test-sets.md).
3. **Improve metrics or methodology.** MAPE, top-1 accuracy,
   per-category breakdowns, bias audits.
4. **Code quality.** Refactors, typing, docs, CI, Python-version support.

## Local development

```bash
git clone https://github.com/foodvision-bench/foodvision-bench
cd foodvision-bench
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
```

## PR checklist

- [ ] `pytest` passes locally.
- [ ] `ruff check .` passes.
- [ ] If you added a system adapter, its docstring says whether results are
      vendor-reported or independently measured, and lists the test set used.
- [ ] If you touched the leaderboard, you added or updated a file under
      `benchmarks/results/` with raw numbers that back up the change.
- [ ] Commit messages are clear. Reference issues with `Closes #N` where
      relevant.

## Reporting a number that disagrees with ours

If you re-ran one of the adapters and got a materially different result,
please open an issue with:

- The exact commit SHA you ran against
- The test set you used
- Your raw results JSON (the same format as `benchmarks/results/*.json`)
- Your environment (OS, Python, CUDA if any)

We would rather correct a bad number than defend it.

## Code of conduct

By participating you agree to abide by the
[Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).
