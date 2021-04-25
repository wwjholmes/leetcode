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
        m = len(p)
        n = len(s)
        # two dimension 
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            match_any = False
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = True if j == 0 else False
                elif j == 0:
                    dp[i][j] = True if p[:i] == Solution.ASTERRISK else False
                elif p[i-1] == Solution.QUESTION_MARK:
                    dp[i][j] = dp[i-1][j-1]
                elif p[i -1] == Solution.ASTERRISK:
                    for k in range(j + 1):
                        if dp[i-1][k]:
                            dp[i][j] = True
                            break
                else:
                    dp[i][j] = dp[i-1][j-1] and p[i-1] == s[j-1]
                match_any |= dp[i][j]
            if not match_any:
                return False

        # print(dp)
        return dp[-1][-1]

    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 



# @lc code=end
s = "aa"
p = "*"
s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
p = "a*******b"
s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
s = "acdcb"
p = "a*c?b"
s = "adceb"
p = "*a*b"
s = "abbaaaabbbbbababbbabaaabbabbbabbbbabbaaabbabaaabbbbabbbabaaaababaaaaaaabbaabaaaabbababbabbabbaabaabaaabbababaabbabaaaaabbbaabaaaabaabababbbbbabbbbabbaabbabbabbabbaabbabababbbbabbbabbbbbbababbbabaaaabaab"
p = "****aa*****a**b***b****bab*b*baab**b*ba*a*****ba***bb**ba******a*bbb****bbb*a*****a*b*abb**aabb***aa"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
p = "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"
sol = Solution()
print(sol.isMatch(s, p))
