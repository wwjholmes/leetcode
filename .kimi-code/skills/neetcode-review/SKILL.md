---
name: neetcode-review
description: Review a completed NeetCode/LeetCode practice attempt in this repository as a senior/staff engineer would in a live coding interview debrief. Use only when the user explicitly invokes `/skill:neetcode-review`; evaluates correctness, readability, efficiency, and test coverage, in that priority order.
disableModelInvocation: true
---

# NeetCode Solution Review

Review the user's solution (and tests, if present) as a senior/staff engineer
would in a live coding interview debrief. The user prioritizes correctness and
readability over cleverness — this is a 30–45 minute interview, not a
perfection exercise.

## Setup

1. Read the repository's `AGENTS.md` for project conventions.
2. Identify the target problem module in `problems/` (and its test in `tests/`
   if one exists). If the user supplied a path or problem number, use it;
   otherwise use the most recently modified module. If ambiguous, ask.
3. Run the relevant tests before reviewing:

   ```bash
   python -m unittest discover -s tests -v
   ```

## Evaluation Order

1. **Correctness** — Does it handle all stated constraints and edge cases? Walk
   through the logic; flag bugs with a concrete failing input, not vague
   concerns.
2. **Readability & maintainability** — Naming, control flow, structure. Would a
   strong engineer understand this in one read? Suggest concrete
   simplifications, not stylistic rewrites.
3. **Efficiency** — State the actual time/space complexity. If worse than
   optimal, explain the gap briefly; do not push micro-optimizations that hurt
   clarity.
4. **Test coverage & clarity** — Do the tests cover the representative case,
   boundaries, and contract invariants? Point out the single most valuable
   missing test.

## Rules

- Be direct and concise; no flattery, no filler.
- Rank findings by severity. Distinguish "would fail the interview" from
  "nice-to-have polish."
- Do not rewrite the whole solution — show minimal diffs for suggested changes.
- Apply changes to files only if the user asks; the review itself is read-only
  apart from running tests.
- End with a 2–3 sentence verdict: would this pass a senior/staff loop, and
  what is the single most important thing to fix or verbalize next time.

## After the Review

Once the user has seen the verdict and any follow-up changes are settled, offer
to record the attempt in `notes/neetcode75.md` (pattern, time/space complexity,
mistakes, missed test cases) per `AGENTS.md`. Do not update the notes file
unprompted.
