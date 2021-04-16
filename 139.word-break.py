#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (41.68%)
# Likes:    6395
# Dislikes: 304
# Total Accepted:    743.3K
# Total Submissions: 1.8M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        elegible = [True if i == 0 else False for i in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(i):
                if elegible[j] and s[j:i] in word_set:
                    elegible[i] = True
        return elegible[-1]

        
# @lc code=end

# sol = Solution()
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "leetcode"
# wordDict = ["leet","code"]
# print(sol.wordBreak(s, wordDict))
