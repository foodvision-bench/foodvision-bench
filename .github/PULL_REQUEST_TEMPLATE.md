<!--
Thanks for contributing to foodvision-bench. The bar for this repo is
"methodology first, code style second". Please keep the PR description
honest about what was measured and how.
-->

## Summary

<!-- One or two sentences describing the change. -->

## Type of change

- [ ] Bug fix
- [ ] New system adapter
- [ ] New test set
- [ ] Metrics / methodology change
- [ ] Docs / CI / tooling only

## Checklist

- [ ] `pytest` passes locally.
- [ ] `ruff check .` passes.
- [ ] If this adds a system adapter, its docstring states whether results
      are vendor-reported or independently measured, and names the test set.
- [ ] If this touches the leaderboard, the PR also updates
      `benchmarks/results/*.json` with the raw numbers that back up the
      change.
- [ ] Commit messages reference the issue being addressed with `Closes #N`
      where relevant.

## Test plan

<!--
How did you verify the change? Include commands, logs, or links.
If you re-ran a benchmark, include the environment (OS, Python, hardware).
-->
