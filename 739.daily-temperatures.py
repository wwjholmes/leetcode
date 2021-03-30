#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (64.58%)
# Likes:    4010
# Dislikes: 122
# Total Accepted:    229.4K
# Total Submissions: 354.2K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#
from typing import List
# @lc code=start


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        warmer = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                warmer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return warmer


s = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(T))


# @lc code=end
