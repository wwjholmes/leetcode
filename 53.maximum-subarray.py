#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.73%)
# Likes:    11472
# Dislikes: 552
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        sub_sum = -1 
        for n in nums:
            if sub_sum > 0:
                max_sum = max(max_sum, sub_sum + n)
                sub_sum = max(sub_sum + n, 0)
            else:
                sub_sum = n
                max_sum = max(max_sum, n)
        return max_sum


        
# @lc code=end

s = Solution()
nums = [5,4,-1,7,8]
nums = [1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))
