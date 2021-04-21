#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (49.23%)
# Likes:    878
# Dislikes: 1048
# Total Accepted:    83.2K
# Total Submissions: 167.9K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given an array of strings words representing an English Dictionary, return
# the longest word in words that can be built one character at a time by other
# words in words.
# 
# If there is more than one possible answer, return the longest word with the
# smallest lexicographical order. If there is no answer, return the empty
# string.
# 
# 
# Example 1:
# 
# 
# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w",
# "wo", "wor", and "worl".
# 
# 
# Example 2:
# 
# 
# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the
# dictionary. However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.
# 
# 
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        h = defaultdict(list)
        words_set = set(words)
        max_len = 0
        for w in words:
            h[len(w)].append(w)
            max_len = max(max_len, len(w))

        def canBuiltFromOtherWord(w: str) -> bool:
            if len(w) == 1 and w in words_set:
                return True

            for i in range(len(w)):
                new_w = w[:i] + w[i+1:len(w)]
                if new_w in words_set:
                    if canBuiltFromOtherWord(new_w):
                        return True
            return False
        
        while max_len:
            sub = h[max_len]
            sub.sort()
            for w in sub:
                if canBuiltFromOtherWord(w):
                    return w
            max_len -= 1

        return ""

        
# @lc code=end

words = ["a", "banana", "app", "appl", "ap", "apply", "apple", "b"]
words = ["w","wo","wor","worl","world"]
s = Solution()
print(s.longestWord(words))
