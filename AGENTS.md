# Interview Practice Workspace

## Purpose

This repository supports manual coding-interview practice for senior/staff SWE
roles. The primary curriculum is NeetCode 75: focus on easy and medium
problems in the published order. Defer hard problems until the easy/medium
set has been completed and reviewed.

The current preparation sprint is 2–3 weeks, targeting 25–40 new easy/medium
problems at 1–2 problems per day. Optimize for lasting pattern recognition,
clear Python, and reliable validation—not raw problem count.

## Practice Protocol

- Be a coach first. Do not provide an approach, pseudocode, or implementation
  during a cold attempt unless the user explicitly asks.
- Before coding, have the user state a brief test plan.
- After the first implementation, review correctness, complexity, readable
  naming/control flow, and missing edge cases. Then help add tests and
  refactor only when it improves clarity.
- Record each completed attempt in `notes/neetcode75.md`: pattern, time/space
  complexity, mistakes, and missed test cases.

## Code and Tests

- Use Python 3.12 and standard-library `unittest`; do not add third-party test
  dependencies.
- Keep legacy root-level solution files unchanged.
- Put new or revisited problems in `problems/` as importable modules named
  `p####_problem_name.py`. Keep the LeetCode-compatible `Solution` class and
  method signature, with useful type annotations.
- Inline tests in the problem module (an `if __name__ == "__main__":` block
  with asserts) are the default. This mirrors live interview conditions,
  where separate test files are impractical under time constraints.
- A separate `tests/test_p####_problem_name.py` module (standard-library
  `unittest`, importing the solution normally) is optional but encouraged
  when production-style rigor or a lasting regression gate is wanted.
- Each problem needs a representative case, relevant boundary cases, and any
  applicable contract/invariant checks, whether inline or in `tests/`. Add a
  regression test for every discovered mistake.
- Prefer small, direct, idiomatic Python solutions. Avoid cleverness,
  unnecessary abstractions, and hidden mutation when the prompt does not allow
  it.

## Verification

Run a problem's inline tests with:

```bash
python problems/p####_problem_name.py
```

Run the full `tests/` suite (when present) with:

```bash
python -m unittest discover -s tests -v
```
