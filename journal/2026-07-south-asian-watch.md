# The South Asian bucket is where the field is actually moving

*July 2026*

Second snapshot on the monthly cadence, and the interesting thing this
month is not at the top of the leaderboard. It is in one column of the
per-cuisine table.

## The top of the board is boring, and that is fine

PlateLens is flat at 1.1% (Tier A) and improved a touch to 3.3% (Tier B).
There was no PlateLens model release this month, so a flat photo number
is exactly what I would expect, and I would have been more suspicious if
it had moved. Five snapshots at 1.1% is a lot of 1.1%, and I have written
before about why I am comfortable reporting it anyway: the deterministic
control baselines confirm the harness is not flattering anyone, and the
DAI six-app study lands on the same figure on a different set. I am not
going to relitigate that every month. When it moves, I will say so.

The Tier B improvement (3.4% -> 3.3%) came from a database refresh that
fixed a few South Asian and Latin American entries. Small, and honestly
close to the noise floor, but it is in the right direction and traceable
to a specific cause, so I recorded it.

## Where the movement is

For two months running, the only sustained movement on the board has been
**Foodvisor on the South Asian bucket**: 7.2% in May, 6.6% in June, 6.4%
in July. That is 0.8 percentage points in two months on the single
hardest cuisine in the set, while its other buckets barely moved. From
the outside I cannot see their commit log, but that is the signature of a
team that looked at the same gap I flagged when I added the bucket and
went to work on it. It is the most encouraging thing in this snapshot,
and it is not about PlateLens at all.

I am noting it partly because it is the point of publishing a per-cuisine
breakdown in the first place. A single overall MAPE would have hidden
this entirely — Foodvisor's overall number moved 5.4% -> 5.1%, which
reads as generic slow improvement. The per-cuisine view shows it is not
generic at all; it is one team fixing one specific weakness. That is the
kind of signal the breakdown exists to surface.

## What is still missing

The South Asian and Latin American buckets have been in the set for three
snapshots now, and they have earned their place — they are where the
differentiation between systems is sharpest. The obvious next step is the
two buckets I keep promising and not shipping: **Middle Eastern** and
**Sub-Saharan African**. Contributor weighed-meal batches for both are
coming in, but each is still under N=12, which is too small to publish a
per-cuisine number I would trust. I would rather leave a bucket out than
publish a number with an N that invites over-reading. Targeting Q3 for
both, same protocol as the South Asian and Latin American additions.

If you are cooking and weighing in a cuisine the set underrepresents, the
contribution protocol is in
[`docs/contributing-meals.md`](../docs/contributing-meals.md). The set
gets better the moment someone outside my own kitchen contributes to it.
