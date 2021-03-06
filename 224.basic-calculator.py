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
import re

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

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        # split str to compose a infix notation expression
        infix = re.findall('[+-/*//()]|\d+',s)
        print(infix)

        # infix notation => postfix notation
        suffix = []
        opeartors = []

        while infix:
            val = infix.pop(0)
            if val.isdigit():
                suffix.append(val)
            elif val == PLUS or val == MINUS:
                while opeartors:
                    if PRIORITY[opeartors[-1]] > 0 and PRIORITY[opeartors[-1]] >= PRIORITY[val]:
                        suffix.append(opeartors.pop(-1))
                    else:
                        break
                opeartors.append(val)
            elif val == LEFT_PARENTHESES:
                opeartors.append(val)
            elif val == RIGHT_PARENTHESES:
                while opeartors:
                    if opeartors[-1] == LEFT_PARENTHESES:
                        opeartors.pop()
                        break
                    else:
                        suffix.append(opeartors.pop())
        # append all rest of operators
        opeartors.reverse()
        suffix.extend(opeartors)

        # calculate based on suffix notation
        digits = []
        while suffix:
            val = suffix.pop(0)
            if val == PLUS:
                a = int(digits.pop(0))
                b = int(digits.pop(0))
                digits.append(a + b)
            elif val == MINUS:
                a = int(digits.pop(0))
                b = int(digits.pop(0))
                digits.append(a - b)
            else:
                digits.append(val)

        return digits.pop(0)
        
        
s = Solution()
infix = "1 + 1"
infix = "(1+(4+5+2)-3)+(6+8)"
print(s.calculate(infix))
# @lc code=end

