# NeetCode 75 Progress Journal

## How to use this journal

Add one short entry after each completed practice session. Record the problem
in NeetCode's published order and keep the emphasis on reusable interview
lessons rather than a full solution write-up.

## Entry template

### `p####` — Problem name

- **Pattern:**
- **First-attempt result / time:**
- **Time / space complexity:**
- **What I got wrong or hesitated on:**
- **Tests or edge cases I initially missed:**
- **Retry cue:**

## Entries

### `p0242` — Valid Anagram

- **Pattern:** Character-frequency comparison; first attempt used sorting.
- **First-attempt result / time:** Correct sorting solution; time not recorded.
- **Time / space complexity:** `O(n log n + m log m)` time and `O(n + m)` space.
- **What I got wrong or hesitated on:** Distinguishing quick inline assertions from formal `unittest` coverage; initially added unnecessary `None` checks outside the problem contract.
- **Tests or edge cases I initially missed:** Same-length strings with the same distinct letters but different frequencies (for example, `"aacc"` and `"ccac"`).
- **Retry cue:** Verify character counts, not merely whether both strings contain the same kinds of letters.

### `p0125` — Valid Palindrome

- **Pattern:** Two pointers converging from both ends, skipping non-alphanumerics.
- **First-attempt result / time:** Correct two-pointer solution; time not recorded.
- **Time / space complexity:** `O(n)` time, `O(1)` space after review (first attempt was `O(n)` space due to `lower()` copy).
- **What I got wrong or hesitated on:** Asymmetric skip-loop bounds (`i < j` on the left, `j > 0` on the right) rescued by an `if i > j: return True` branch — correct but convoluted; also carried an unnecessary `strip()` and a `lower()` full-string copy.
- **Tests or edge cases I initially missed:** Digits mixed with case-insensitivity (for example, `"0P"` is not a palindrome).
- **Retry cue:** Bound both skip loops with `i < j`; lowercase per character instead of copying the string.
