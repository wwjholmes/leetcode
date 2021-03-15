#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.49%)
# Likes:    9975
# Dislikes: 661
# Total Accepted:    1.2M
# Total Submissions: 4M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        length = len(s)
        for i in range(len(s)):
            for (left, right, count) in [(i-1, i+1, 1), (i, i+1, 0)]:
                while left >= 0 and right <= length - 1 and s[left] == s[right]:
                    count += 2
                    left -= 1
                    right += 1
                p_length = right - left - 1
                longest = s[left +
                            1: right] if p_length > len(longest) else longest
        return longest


# sol = Solution()
# s = "ac"
# s = "babad"
# print(sol.longestPalindrome(s))

        
# @lc code=end

