---
name: Propose a new system to benchmark
about: Nominate a model or commercial API for inclusion in the leaderboard
title: "[system] add <name>"
labels: adapter
assignees: ''
---

## System name

## Kind

- [ ] Open-source model (runnable directly, independently measured)
- [ ] Commercial API / app (vendor-reported or replicated)

## Where to find it

- Paper / model card / HF model page:
- Pricing (if commercial):
- License:

## Proposed adapter

Sketch of how `FoodRecognitionSystem.identify` / `estimate_portion` would be
implemented. For vendor systems, identify where the numbers come from and
whether they are vendor-reported or replicated.

## Ground-truth strategy

Which test set(s) from `docs/test-sets.md` would this adapter be evaluated
against? If a new test set is needed, please open a separate issue first.

## Checklist

- [ ] The system can be identified unambiguously (name + version + date).
- [ ] At least one test set applies.
- [ ] Numbers are either reproducible locally or clearly labelled as
      vendor-reported.
- [ ] A maintainer has time to review the PR (rough ETA).
