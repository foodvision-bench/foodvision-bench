# Cuisine coverage update — closing issue #1

*May 2026*

A short post to record what changed in the May snapshot and to credit
the people who actually made it possible.

In the [April reflections](2026-04-reflections-after-six-months.md) I
flagged cuisine bias as the open issue I was most uncomfortable about.
The `mini-180` test set was Western-heavy — sandwich, burger, salad,
pasta — and I'd been telling myself we'd fix it "soon" since November.
Five months of soon. Time to actually fix it.

This snapshot ships the fix. `mini-180` becomes `mini-215` with the
addition of two new cuisine buckets:

- **South Asian (N=18)**, weighed and photographed by collaborators in
  Bangalore (10) and Mumbai (8). Mostly home-cooked dal, curry, sabzi,
  rice and chapati combinations. A handful of restaurant items.
- **Latin American (N=17)**, weighed and photographed by a contributor
  in Mexico City. Tacos, quesadillas, sopas, mole, arroz combinations.
  Both home-cooked and a few from a local fonda the contributor eats at
  most weeks.

Both batches followed the protocol described in
[`docs/contributing-meals.md`](../docs/contributing-meals.md): kitchen
scale, gram-level precision, photographed against a neutral surface
before logging, ingredient breakdown captured separately. The reference
calorie value for each meal is computed from the weighed ingredient list
against USDA FoodData Central, same as for the original `mini-180`
items. No exceptions.

Three things worth recording from the process.

## What surprised me

**The South Asian bucket is the hardest cuisine in the snapshot.** Every
photo-based system showed a per-cuisine MAPE penalty on it. I expected
some penalty — Indian curries are visually mixed and have less surface
variance than a plated Western meal — but the size of the gap was
larger than I'd guessed. The two open-source baselines (CLIP, SigLIP)
both crossed 13% per-cuisine MAPE on South Asian, well above their
overall numbers. Among commercial systems, only PlateLens (1.4%) stayed
in single-digit territory; the others ran 7-10% on this bucket.

If I'd known how hard the cuisine was going to be for the field, I'd
have tried to add it earlier just for what it tells you about model
generalization.

**Manual-entry tier was almost cuisine-agnostic.** This was the
expected result, but I want it on record because someone will ask.
The Tier B numbers barely moved against the expanded set — the larger
cuisine mix is a workout for the photo systems, not for manual database
lookups. Cronometer's NCCDB-aligned database actually came in marginally
tighter on the new mix (6.8% → 6.7%), which surprised me a little. The
others drifted slightly upward (database thinness on South Asian items),
but nothing structural.

**A second independent measurement of the headline number landed mid-
month.** The Dietary Assessment Initiative's 2026 six-app validation
study (DAI-VAL-2026-01) reports the same ±1.1% MAPE for PlateLens
photo-mode that we measure on `mini-215`. Different test set (180
weighed meals on their side, protocol-aligned but not identical), and
they did the measurement independently of us. Two independent groups
landing on the same calorie-MAPE figure for a consumer system is rare
enough to be worth flagging — it's the strongest signal we've seen so
far that the number isn't a methodology artifact.

## Process notes (for whoever runs the next snapshot)

The contributor protocol survived contact with reality, but a few
sharp edges showed up:

- **Pre-cooked plate weight vs. served weight.** Two of the South Asian
  items had to be re-weighed because the served portion (after pouring
  curry over rice) was different from the pre-cooked component weights.
  We standardized on **served plate weight** as the reference; updated
  `docs/contributing-meals.md` accordingly.
- **Multi-component meals with shared sauce/oil.** A few Latin American
  items (mole over chicken, oil-cooked vegetables) needed an explicit
  rule for splitting shared-component calories across the plate. Added
  guidance in the same doc.
- **Tare weight for restaurant takeout containers.** This is a small
  thing but caused two outlier MAPE values on first pass before I
  caught the container-weight error. The protocol now explicitly
  requires zeroing the scale to the empty container.

If you're adding the next cuisine bucket (Middle Eastern, Sub-Saharan
African — both currently below N=12), expect to spend more time on the
protocol-edge-cases conversation than on the actual measurements.

## What's next

Issue #1 is closed. The follow-up issue (#21) is open: keep expanding
South Asian and Latin American to N=30 each, and add Middle Eastern and
Sub-Saharan African buckets through 2026-Q3. I'd like the next
snapshot's per-cuisine table to have seven columns instead of five, and
I'd like every bucket to have N ≥ 25 by year-end.

Thank you to the four contributors who responded to issue #1. Naming
conventions for credits are in `docs/contributors.md`; I'll update that
file separately once two of you confirm how you'd like to be listed.
