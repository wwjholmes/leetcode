#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (37.89%)
# Likes:    1536
# Dislikes: 521
# Total Accepted:    277.8K
# Total Submissions: 726.5K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
# 
# Note that division between two integers should truncate toward zero.
# 
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
# 
# 
# Example 1:
# 
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
# 
# 
#
from typing import List
# @lc code=start

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                stack.append(int(t))
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                # print(a, t, b)
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    if a * b > 0:
                        stack.append(a // b)
                    else:
                        stack.append(-1 * (-a // b))
                else:
                    raise Exception("unexpected symbol")
            # print(stack)
        assert len(stack) == 1, "invalid evaluated result"
        return stack.pop()


# @lc code=end

# s = Solution()
# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["2", "1", "+", "3", "*"]
# tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["4","-2","/","2","-3","-","-"]
# print(s.evalRPN(tokens))
