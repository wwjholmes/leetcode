"""Tests for LeetCode 242: Valid Anagram."""

import unittest

from problems.p0242_valid_anagram import Solution


class ValidAnagramTests(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_anagrams_with_different_ordering(self) -> None:
        self.assertTrue(self.solution.isAnagram("abc", "cba"))

    def test_anagrams_with_repeated_characters(self) -> None:
        self.assertTrue(self.solution.isAnagram("abbc", "cbab"))

    def test_non_anagrams_with_same_length(self) -> None:
        self.assertFalse(self.solution.isAnagram("abc", "xyz"))

    def test_same_letters_with_different_frequencies_are_not_anagrams(self) -> None:
        self.assertFalse(self.solution.isAnagram("aacc", "ccac"))

    def test_empty_strings_are_anagrams(self) -> None:
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_strings_with_different_lengths_are_not_anagrams(self) -> None:
        self.assertFalse(self.solution.isAnagram("ab", "abc"))

    def test_empty_and_nonempty_strings_are_not_anagrams(self) -> None:
        self.assertFalse(self.solution.isAnagram("", "cbab"))


if __name__ == "__main__":
    unittest.main()
