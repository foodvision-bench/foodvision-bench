# Why we use MAPE over absolute kcal error

*December 2025*

A reviewer asked why the leaderboard's headline metric is MAPE (Mean
Absolute Percent Error) rather than absolute kilocalorie error. Fair
question — and one that's worth writing down, because the choice has
non-obvious consequences for how systems are ranked.

## The simple answer

Meals vary wildly in total energy content. A roasted-vegetable plate
might come in at 180 kcal. A loaded burrito might be 1,100 kcal. A
system that is consistently off by ±50 kcal looks excellent on the
burrito (4.5% relative error) and catastrophic on the salad (27.8%
relative error). If we rank systems on absolute-kcal error, we
implicitly reward systems that happen to perform better on high-energy
meals — which, in practice, tends to reward systems that have memorized
a narrow slice of the American diet.

MAPE normalizes each error by the meal's true energy, so a 5% error on
a 200-kcal dish contributes the same as a 5% error on a 1,000-kcal
dish. That matches what users actually care about: "is this app's
number roughly right for the meal I just ate?"

## The harder answer

MAPE has real downsides:

1. **It's unstable for very-low-kcal items.** A cup of black coffee
   (~2 kcal) with a 10 kcal estimate gives a 400% error. We handle
   this by excluding items below a 30-kcal floor from the aggregate —
   documented in `docs/methodology.md`.

2. **It treats over- and under-estimates symmetrically.** For some
   applications (e.g., medical nutrition tracking) a systematic
   under-estimate is much worse than a systematic over-estimate. We
   report signed mean error separately in the per-system JSON output
   for callers who need it.

3. **It doesn't decompose cleanly across meal components.** If a
   system is great at main dishes and terrible at sides, MAPE hides
   the structure. The per-category breakdown is the right place to
   look for that detail, not the headline number.

## What we considered and rejected

- **RMSE on kcal.** Over-weights high-energy meals.
- **Log-space error.** More defensible statistically, but hostile to
  non-statistician readers; we don't want the headline metric to
  require a paragraph of explanation.
- **Top-1 only.** Some systems (Cronometer, MyFitnessPal) don't do
  classification in a conventional sense, so top-1 isn't defined for
  them. MAPE works everywhere we can estimate kcal.

## Bottom line

MAPE is not perfect. It is the least-bad default we found for a
mixed-methodology leaderboard that has to span both classification
models and end-to-end nutrition apps. If you have a better suggestion,
open an issue — we will consider it for v0.3.

— The maintainer
