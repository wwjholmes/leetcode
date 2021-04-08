#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.57%)
# Likes:    15912
# Dislikes: 578
# Total Accepted:    3.1M
# Total Submissions: 6.8M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in h:
                return [h[k], i]
            else:
                h[nums[i]] = i
        raise Exception("No solution found")


# @lc code=end
# s = Solution()
# nums = [2, 7, 11, 15]
# target = 9
# print(s.twoSum(nums, target))
