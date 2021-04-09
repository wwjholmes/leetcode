#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (58.54%)
# Likes:    5330
# Dislikes: 167
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # index of current num being in processing 
        zindex = -1  # index of the very first position of 0
        while left < len(nums) and zindex < len(nums):
            if nums[left] == 0:
                if zindex == -1:
                    zindex = left
                left += 1
            else:
                if zindex != -1:
                    nums[zindex] = nums[left]
                    nums[left] = 0
                    zindex += 1
                left += 1


# @lc code=end
