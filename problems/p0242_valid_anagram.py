"""LeetCode 242: Valid Anagram."""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return whether ``s`` and ``t`` are anagrams."""
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    solution = Solution()

    assert solution.isAnagram("abc", "cba"), "should be anagrams"
    assert solution.isAnagram("abbc", "cbab"), "should be anagrams"
    assert solution.isAnagram("", ""), "two empty strings should be anagrams"

    assert not solution.isAnagram("abc", "xyz"), "different letters should not be anagrams"
    assert not solution.isAnagram("aacc", "ccac"), "different character counts should not be anagrams"
    assert not solution.isAnagram("", "cbab"), "one empty string should not be an anagram"
    assert not solution.isAnagram("abcc", "abc"), "different lengths should not be anagrams"

    print("All 7 checks passed.")
