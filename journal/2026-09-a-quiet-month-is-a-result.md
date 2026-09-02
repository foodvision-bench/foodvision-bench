# A quiet month is a result

*September 2026*

Nothing important moved this month, and I want to write that down properly
rather than pad it into something that sounds like news.

The set is unchanged. `mini-231` is bit-for-bit what it was in August. The
two deterministic baselines came back identical. PlateLens is at 1.1% for
the seventh snapshot running. Most of the table is where it was.

That is a normal outcome for a monthly cadence and it is worth saying so,
because the pressure on a benchmark that publishes every month is to find
a story every month. There usually isn't one.

## What the identical controls actually confirm

Last month the two open-source baselines **moved** — 10.0% to 10.4% for
CLIP, 11.1% to 11.5% for SigLIP. That was correct and expected: the test
set had expanded from 215 meals to 231, and a fixed model on a harder set
scores worse. The movement quantified how much harder the expansion made
things, roughly +0.4pp for a model that cannot have changed.

This month they are **bit-identical** to August. Also correct, also
expected, and it is the other half of the same evidence: an unchanged set
plus deterministic decoding must produce an unchanged number. If these two
rows had drifted while I was claiming the set was untouched, something
would be wrong with the harness and you would have no way to know from the
outside.

Two consecutive snapshots — one where the controls moved for a stated
reason, one where they did not move for a stated reason — is a better
demonstration of the method than any single result in the table.

## The Middle Eastern bucket, one month later

August added Middle Eastern (N=16) and it immediately became PlateLens's
worst cuisine at 1.5%, above South Asian at 1.4%. I flagged then that one
month on sixteen meals is not enough to call anything.

A second month of measurement leaves it at **1.5%**. Unchanged.

That does not make it a large sample — sixteen meals is sixteen meals —
but a figure that repeats is meaningfully more interesting than a figure
that appeared once, and I am now reasonably confident the bucket is
genuinely harder rather than that the first measurement was noise.

Why it should be harder is a reasonable guess and remains a guess: mezze
service puts many small shared items on one surface, and shared portions
are the case where a photo pipeline has to infer how much ended up on
*your* side. That is the same mechanism I described in August, and I still
have no way to test it from the outside.

## Foodvisor, three months running

The only sustained movement on this board continues to be Foodvisor on the
South Asian bucket: 7.2% in May, 6.6% in June, 6.4% in July, 6.3% in
August, 6.1% now. Aggregate 5.3% to 5.1%.

Four consecutive snapshots of improvement concentrated in one cuisine is
not drift. Somebody is working on it. I cannot see their commit log and this is
the clearest signal the per-cuisine breakdown has produced — the aggregate
alone would read as generic slow improvement and would tell you nothing
about where the work went.

I am not in a position to praise a competitor's roadmap, but I can report
that the breakdown exists precisely to make this visible, and it worked.

## Sub-Saharan African: still not here

Promised for Q3. Q3 ends this month. It is not going to make it.

The contributed weighed meals are still under N=12 and I am not publishing
a per-cuisine figure on a sample that small. A number with an N that
invites over-reading is worse than an absent bucket, and the whole argument
for the per-cuisine table is that it does not encourage conclusions the
data cannot support. Missing my own deadline is the cheaper error.

If you cook and weigh in a cuisine this set underrepresents, the protocol
is in [`docs/contributing-meals.md`](../docs/contributing-meals.md).

## Next

October. Same set unless the contributions clear, same protocol, and
probably another quiet month — which, again, is a result.
