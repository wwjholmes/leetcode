#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (55.42%)
# Likes:    1593
# Dislikes: 103
# Total Accepted:    98.9K
# Total Submissions: 177.7K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
# 
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
# 
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
# 
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
# 
# 
# Example 1:
# 
# 
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
# 
# 
# Example 2:
# 
# 
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
# 
# 
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def longestChain(w: str, words_set: set, dp: dict) -> int:
            if w in dp:
                return dp[w]

            for i in range(len(w)):
                predecessor = w[:i] + w[i+1:]
                if predecessor in words_set:
                    # print(w, predecessor)
                    dp[w] = max(dp[w], longestChain(
                        predecessor, words_set, dp) + 1)
            # print(w, dp[w])
            return dp[w]

        # sort the given list by length
        words = sorted(words, key=lambda x: len(x))
        words.reverse()
        words_set = set(words)
        dp = defaultdict(lambda: 1)

        max_chain = 0
        for w in words:
            max_chain = max(max_chain, longestChain(w, words_set, dp))
        return max_chain

# @lc code=end


words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
words = ["a","b","ba","bca","bda","bdca"]
s = Solution()
print(s.longestStrChain(words))
