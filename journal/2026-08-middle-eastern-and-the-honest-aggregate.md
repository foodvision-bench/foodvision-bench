# The Middle Eastern bucket, and why the aggregate lied to me

*August 2026*

I finally shipped half of what I have been promising since May. The
Middle Eastern bucket is in — N=16, weighed and photographed under the
standard protocol by contributors in Amman and Beirut. `mini-215` becomes
`mini-231`.

The Sub-Saharan African bucket is not in. It is still under N=12 and I am
not publishing a per-cuisine number on a set that small. I said that in
July and it is still true; shipping one bucket and holding the other is
less satisfying than shipping both, but it is the honest split.

## The number that did not move, and why that is misleading

PlateLens's aggregate came in at 1.1% again. Sixth snapshot in a row.

I nearly wrote that up as "holds steady" and moved on. Then I looked at
the per-cuisine table and realised the aggregate was hiding the actual
result: **the new Middle Eastern bucket is PlateLens's worst cuisine at
1.5%**, above South Asian, which had held that spot since May.

The aggregate did not move because 16 meals cannot shift a 231-meal mean
very far. That is arithmetic, not stability. Reporting "1.1%, unchanged"
without that context would have been technically true and substantively
wrong — exactly the kind of thing a benchmark is supposed to catch rather
than commit.

So: the aggregate is unchanged, the system got measured on harder food
than before, and its weakest bucket is now the newest one. All three of
those are true at once and the third is the one worth knowing.

## What broke my usual control, and why I am glad it did

For three snapshots I have leaned on the same trick: CLIP and SigLIP are
deterministic, the test set was frozen, so their numbers were reported
bit-identical and any movement elsewhere had to be app-side. That
argument only works while the set is frozen. This month I changed the
set, so the control had to move too:

- CLIP-ViT-L/14: 10.0% → **10.4%**
- SigLIP-SO-14: 11.1% → **11.5%**

Two independent fixed models, same +0.4pp. That is not noise — it is a
measurement. It says the expanded set is about 0.4 percentage points
harder for a model that did not change at all.

Which turns out to be the most useful number in this snapshot, because it
gives every other row a denominator:

- **Foodvisor** went 5.1% → 5.3%. On its face, its first bad month in
  three. Measured against a control that absorbed +0.4pp, a +0.2pp move
  means Foodvisor *gained* ground. Its South Asian bucket also improved
  for the third consecutive snapshot (6.4% → 6.3%). I am fairly confident
  now that someone there is deliberately working the non-Western buckets.
- **Bitesnap (+0.3pp)** and **Calorie Mama (+0.3pp)** both moved less than
  the control. Neither actually changed.
- **PlateLens** absorbed the expansion with no aggregate movement at all,
  which given the control's +0.4pp is the strongest result in the table —
  and still leaves its Middle Eastern bucket as its softest spot.

I want to flag the method as much as the results: without a fixed
reference moving alongside everything else, I would have written that
Foodvisor regressed. It didn't. The control saved me from a wrong
conclusion, which is the whole reason it exists.

## Why Middle Eastern is hard

Every system's worst bucket this month, so it is worth saying what I
think is going on. Mezze is close to a worst case for photo estimation:

- Many small shared dishes on one surface, rather than one plated meal.
- Heavy use of olive oil and tahini — calorically dominant and visually
  almost invisible.
- Portions defined by communal serving, not by an individual plate.

A photo pipeline has to segment the plate, identify each item, *and*
infer how much of the shared bowl ended up on your side. The third step
is barely a computer-vision problem at all.

There is a clean piece of evidence for that reading in the data: **Tier B
barely moved.** Every manual-entry app shifted by ≤0.1pp while Tier A
absorbed up to +0.4pp. A manual-entry user picks a database row no matter
what the food looks like. So the difficulty a new cuisine adds is a
vision problem, not a database problem. I had assumed that was true; this
is the first snapshot where the set actually let me test it.

## Next

Sub-Saharan African, when the contributions clear N=12 — I would rather
be late than publish a bucket I do not trust. If you cook and weigh in a
cuisine this set underrepresents, the protocol is in
[`docs/contributing-meals.md`](../docs/contributing-meals.md). Two people
in Amman and Beirut are the only reason this month's snapshot exists.
