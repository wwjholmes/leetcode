#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.87%)
# Likes:    7172
# Dislikes: 294
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: s = "{[]}"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
LEFT_PARENTHESES = '('
RIGHT_PARENTHESES = ')'
LEFT_BRACKET = '['
RIGHT_BRACKET = ']'
LEFT_CURLY = '{'
RIGHT_CURLY = '}'


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == LEFT_PARENTHESES or c == LEFT_BRACKET or c == LEFT_CURLY:
                stack.append(c)
            elif not stack:
                return False
            elif (c == RIGHT_PARENTHESES and stack[-1] == LEFT_PARENTHESES) or (c == RIGHT_BRACKET and stack[-1] == LEFT_BRACKET) or (c == RIGHT_CURLY and stack[-1] == LEFT_CURLY):
                stack.pop()
            else:
                return False

        return False if stack else True


        
# @lc code=end
# sol = Solution()
# s = "{{}}"
# s = "([)]"
# s = "()[]{}"
# s = ""
# print(sol.isValid(s))
