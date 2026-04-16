# Reflections after six months

*April 2026*

Foodvision Bench started in early November 2025. It's been five-and-
a-bit months. About thirty commits, a CHANGELOG that now spans five
tagged releases, a handful of filed issues, and some early community
interest that's been more thoughtful than I expected. Worth writing
down what I've learned before I forget the texture of the early
period.

## What went right

**Picking MAPE as the headline metric.** Every time someone has
written in with methodology questions, the conversation has been
constructive, not combative. I credit this partly to the explainer
in `docs/interpreting-mape.md`: if the metric has a clear definition
and known limitations, people engage with the limitations rather
than arguing about whether the metric is fair.

**Separating vendor-reported from replicated numbers.** This was the
single most important design decision. When I added the first
commercial adapter (PlateLens, in February), having a pre-existing
slot for "vendor-reported" meant I didn't have to choose between
refusing to list it and pretending I'd verified the number. The
leaderboard still reads honestly.

**Small test set.** The 180-meal `mini-180` set is too small for
strong statistical claims per cuisine or per meal type. But it's
small enough that a single motivated contributor can actually re-run
it, which is the whole point.

## What I'd do differently

**Cuisine bias.** Issue #1 is open for a reason. The test set skews
Western — sandwich, burger, salad, pasta heavy. I knew this going
in and told myself we'd fix it "soon." Five months later it's still
unfixed. The lesson: if a known limitation is going to take
real-work to fix, put the fix in the original scope, not the
follow-up scope. I'm now actively looking for weighed meal
photography from East Asian and Latin American home kitchens.

**Communication cadence.** I under-invested in the journal for the
first four months. Decisions that I'd have benefited from writing
down at the time — the MAPE vs. absolute-kcal choice, the
vendor-reported vs. replicated split — are harder to reconstruct
now. The right move is to write the journal post at the time of
the decision, even if nobody reads it.

## Where this is heading

- Broader cuisine coverage. This is the biggest known gap.
- Per-cuisine breakdown on the leaderboard (being added this week).
- Replication runs for the vendor-reported-only adapters, as
  resources allow.
- Python 3.13 support (done in CI, #2).
- Maybe a Yazio adapter if someone in the community picks it up (#4).

Not on the roadmap: a hosted web UI, because the whole point of this
being a repo rather than a website is that readers can run it
themselves. If I ever change my mind about that, it'll be documented
here.

Thanks to everyone who's filed an issue, submitted a PR, or quietly
starred the repo. This project is more useful with company.

— The maintainer
