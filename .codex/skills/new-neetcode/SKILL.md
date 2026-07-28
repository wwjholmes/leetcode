---
name: new-neetcode
description: Prepare a blank, LeetCode-compatible Python exercise from a NeetCode problem URL in this interview-practice repository. Use only when the user explicitly invokes `$new-neetcode` and provides a NeetCode problem link; create the typed `Solution` skeleton without an approach, solution, or tests.
---

# New NeetCode Problem

## Workflow

1. Read the repository's `AGENTS.md` before acting.
2. Open the supplied NeetCode question URL. Extract the problem number, title, stated contract, and canonical Python `Solution` method signature. Do not open the solution tab or expose hints, pseudocode, or an algorithm.
3. Normalize the title into `problems/p####_problem_name.py`, using a zero-padded four-digit number and lowercase snake case.
4. Check whether that module already exists. If it does, do not overwrite it; report the existing path and offer cold-attempt coaching or review instead.
5. Create only the starter module:
   - A `"""LeetCode <number>: <title>."""` module docstring.
   - An importable `Solution` class.
   - The typed LeetCode-compatible method signature with a short contract docstring and `raise NotImplementedError`.
6. Do not create a test file, inline assertions, an implementation, an approach, or pseudocode. After scaffolding, ask the user to state a brief test plan before they start coding.

## Contract Resolution

- Use the problem page as the source of truth for return shape, mutability, and constraints.
- Use built-in generic annotations such as `list[int]` and `dict[str, int]` for Python 3.12.
- If the canonical method name or parameter/return contract cannot be determined confidently from the problem page, stop and ask the user rather than guessing.

## Interaction Boundaries

- Treat this as a cold interview attempt: provide only the problem contract needed for the interface, never a solution strategy unless the user explicitly requests one later.
- Respect the user's preference for self-contained inline assertions when they ask for test help; do not add them during scaffolding.
- Leave `notes/neetcode75.md` unchanged until the user has completed and reviewed their attempt.
