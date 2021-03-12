#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (43.47%)
# Likes:    2695
# Dislikes: 136
# Total Accepted:    183K
# Total Submissions: 420.4K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#
from typing import List

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        h = {0: -1}
        max_length = 0
        for i in range(len(nums)):
            sum += 1 if nums[i] == 1 else -1
            if sum in h:
                max_length = max(i - h[sum], max_length)
            else:
                h[sum] = i
        return max_length

s = Solution()
nums = [0,1,1]
nums = [0, 1, 0]
nums = [1, 0]
nums = [0, 0]

print(s.findMaxLength(nums))

# @lc code=end
