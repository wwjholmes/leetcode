#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.14%)
# Likes:    2048
# Dislikes: 163
# Total Accepted:    198.5K
# Total Submissions: 520.1K
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing an expression, implement a basic calculator to
# evaluate it.
# 
# 
# Example 1:
# 
# 
# Input: s = "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# 
# 
#
from typing import List
import re

# @lc code=start


class Solution:
    PLUS = '+'
    MINUS = '-'
    LEFT_PARENTHESES = '('
    RIGHT_PARENTHESES = ')'

    PRIORITY = {
        PLUS: 1,
        MINUS: 1,
        LEFT_PARENTHESES: -100,
        RIGHT_PARENTHESES: -100,
    }

    def calculate(self, s: str) -> int:
        # split str to compose a infix notation expression
        infix = re.findall('[+-/*//()]|\d+',s)
        # print(infix)
        stack = []

        while infix:
            val = infix.pop(0)
            if val != self.RIGHT_PARENTHESES:
                stack.append(val)
            else:
                expression = []
                # pop from stack til left parentheses
                while stack[-1] != self.LEFT_PARENTHESES:
                    expression.append(stack.pop(-1))
                # pop up left parenthese
                stack.pop(-1)
                expression.reverse()
                result = str(self.calculatePlainExpression(expression))
                # append calculated val to stack
                stack.append(result)
                
        return self.calculatePlainExpression(stack)

    def calculatePlainExpression(self, expression: List[str]) -> int:
        # print("expression:", expression)
        stack = []
        while expression:
            token = expression.pop(0)
            if token == self.PLUS:
                a = int(stack.pop(-1)) if stack else 0
                b = int(expression.pop(0))
                stack.append(a + b)
            elif token == self.MINUS:
                a = int(stack.pop(-1)) if stack else 0
                b = int(expression.pop(0))
                stack.append(a - b)
            else: 
                stack.append(token)
        # print("stack:", stack)
        return stack[-1]
        

s = Solution()
infix = "2-(5-6)"
infix = "-2+ 1"
infix = "(1+(4+5+2)-3)+(6+8)"
infix = "1 + 1"
infix = "(5-(1+(5)))"
print(s.calculate(infix))
# @lc code=end

