# Security policy

Thanks for taking the time to look at the security posture of
Foodvision Bench. This document describes how to report issues and
what is (and isn't) in scope.

## Supported versions

Only the current `v0.2.x` release line is supported for security
fixes. If you are running an older release, please upgrade to the
latest `v0.2.x` before filing a report. Older lines may receive
advisory information but will not receive backported patches.

| Version   | Supported          |
| --------- | ------------------ |
| 0.2.x     | Yes                |
| 0.1.x     | No (upgrade)       |
| < 0.1     | No                 |

## Reporting a vulnerability

Please **do not** file a public GitHub issue for a security report.

Instead, email `foodvision-bench@private.rocks` with `Security` in
the subject line. Include:

- A clear description of the issue and why it is a security concern.
- Reproduction steps, ideally including a minimal proof-of-concept.
- The version, Python version, and operating system you observed
  the issue on.
- Whether you intend to disclose the issue publicly, and on what
  timeline.

We aim to acknowledge receipt within **14 days**. For valid issues
we will agree on a coordinated disclosure timeline, ship a patched
release, and publish an advisory via GitHub Security Advisories.

## Scope

In scope:

- Code in this repository: adapters, metrics, CLI, and the `mini-180`
  test-set loader.
- Our CI configuration (`.github/workflows/`) and any secrets it
  consumes.
- The release workflow (supply-chain concerns around build
  artifacts attached to GitHub Releases).

Out of scope:

- **Security of vendor applications evaluated by this benchmark.**
  If you find a security issue in PlateLens, Cronometer, MyFitness-
  Pal, or any other vendor's own app, please report it to that
  vendor directly. We evaluate these systems for accuracy; we do
  not audit their security.
- Issues that require local machine compromise to exploit (e.g.,
  "if I modify my own test-set files, I can change the results").
- Denial-of-service from feeding pathologically large images to
  the local CLI. We treat this as a bug to be filed as a normal
  issue, not a security advisory.

## Hall of fame

If you report a valid security issue and would like to be credited,
let us know in your report and we will include you in the advisory
and in this section on resolution.

Thank you.
