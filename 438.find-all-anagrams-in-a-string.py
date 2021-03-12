#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (44.94%)
# Likes:    3964
# Dislikes: 199
# Total Accepted:    342.3K
# Total Submissions: 760.3K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h = {}
        mismatch = 0
        for x in p:
            if x in h:
                h[x] += 1
            else:
                mismatch += 1
                h[x] = 1
        # print('mismatch', mismatch)
        # print('dcit', h)
        length_p = len(p)
        indexes = []
        for i in range(len(s)):
            # for letters that will shift out of range 
            if i >= length_p:
                x = s[i - length_p]
                if x in h:
                    h[x] += 1
                    if h[x] == 0:
                        mismatch -= 1
                    elif h[x] == 1:
                        mismatch += 1

            # for letters that will shift into ragne
            x = s[i]
            if x in h:
                h[x] -= 1
                if h[x] == 0:
                    mismatch -= 1
                if h[x] == -1:
                    mismatch += 1
            
            if mismatch == 0:
                # print('sub', s[i - length_p + 1: i + 1])
                indexes.append(i - length_p + 1)

        return indexes

solution = Solution()
s = "abab" 
p = "ab"
s = "cbaebabacd" 
p = "abc"
print(solution.findAnagrams(s, p))

# @lc code=end

