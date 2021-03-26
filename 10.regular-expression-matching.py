#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.34%)
# Likes:    5522
# Dislikes: 834
# Total Accepted:    522.3K
# Total Submissions: 1.9M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where: 
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start

DOT = "."
ASTERISK= '*'

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print('s:', s)
        # print('p:', p)
        # all characters have been matched
        if s == p:
            # return True as long as they equals with each other
            return True
        elif not p:
            # if s is empty but p still has more chars
            return False
        
        modifier = p[1] if len(p) > 1 else None

        if modifier == ASTERISK and p[0] == DOT:
            for i in range(len(s) + 1):
                if self.isMatch(s[i:], p[2:]):
                    return True
            return False
        elif modifier == ASTERISK and p[0] != DOT:
            for i in range(len(s) + 1):
                sub = p[0] * i
                if sub == s[:i] and self.isMatch(s[i:], p[2:]):
                    return True
            return False
        elif p[0] == DOT:
            return len(s) >= 1 and self.isMatch(s[1:], p[1:])
        elif p[0] != DOT:
            return s and p[0] == s[0] and self.isMatch(s[1:], p[1:])
        else:
            print("unexpected s:", s, " p:", p)
        return False


# sol = Solution()
# s = "mississippi"
# p = "mis*is*p*."
# s = "ab"
# p = ".*"
# s = "aab"
# p = "c*a*b"
# s = "aa"
# p = "a"
# s = "aa"
# p = "a*"
# s = "a"
# p = "ab*"
# s = "ab"
# p = ".*c"
# s = "a"
# p = ".*..a*"
# print(sol.isMatch(s, p))

        
# @lc code=end

