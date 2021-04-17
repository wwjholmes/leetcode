#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (34.67%)
# Likes:    3082
# Dislikes: 444
# Total Accepted:    318K
# Total Submissions: 896.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# 
# 
# Example 2:
# 
# 
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.wordBreakHelper("", s, wordDict)

    def wordBreakHelper(self, prefix: str, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return [prefix[1:]]
        comb = []
        for w in wordDict:
            if w == s[:len(w)]:
                comb += self.wordBreakHelper(
                    " ".join([prefix, w]), s[len(w):], wordDict)
        return comb



        
# @lc code=end

# sol = Solution()
# s = "catsanddog"
# wordDict = ["cat","cats","and","sand","dog"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# s = "pineapplepenapple"
# wordDict = ["apple","pen","applepen","pine","pineapple"]
# print(sol.wordBreak(s, wordDict))
