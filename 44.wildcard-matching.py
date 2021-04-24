#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (25.40%)
# Likes:    2901
# Dislikes: 140
# Total Accepted:    299.3K
# Total Submissions: 1.2M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
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
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input: s = "acdcb", p = "a*c?b"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
# 
# 
#

# @lc code=start
class Solution:
    QUESTION_MARK = "?"
    ASTERRISK = "*"

    def isMatch(self, s: str, p: str) -> bool:
        p = self.remove_duplicate_stars(p)
        dp = {}
        return self.isMatchHelper(s, p, dp)

    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 

    def isMatchHelper(self, s: str, p: str, dp: dict):
        # print(s, p)
        # if fully matched
        if (s, p) in dp:
            return dp[(s, p)]

        if not s and not p:
            dp[(s, p)] = True
            return dp[(s, p)]

        # not more pattern str could match s
        if s and not p:
            dp[(s, p)] = False
            return dp[(s, p)]

        if p[0] == Solution.QUESTION_MARK:
            if not s:
                dp[(s, p)] = False
            else:
                dp[(s, p)] = self.isMatchHelper(s[1:], p[1:], dp)
        elif p[0] == Solution.ASTERRISK:
            p_res = p[1:]
            for i in range(len(p)):
                if p[i] != Solution.ASTERRISK:
                    p_res = p[i:]
                    break
            
            match = False
            for i in range(len(s) + 1):
                if self.isMatchHelper(s[i: len(s)], p_res, dp):
                    match = True
                    break
            dp[(s, p)] = match
        elif not s:
            dp[(s, p)] = False
        elif s[0] == p[0]:
            dp[(s, p)] = self.isMatchHelper(s[1:], p[1:], dp)
        else:
            dp[(s, p)] = False

        return dp[(s, p)]


# @lc code=end
s = "aa"
p = "*"
s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
p = "a*******b"
s = "acdcb"
p = "a*c?b"
s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
sol = Solution()
print(sol.isMatch(s, p))
