#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (32.75%)
# Likes:    6630
# Dislikes: 219
# Total Accepted:    469.6K
# Total Submissions: 1.4M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
# 
# It is guaranteed that the answer will fit in a 32-bit integer.
# 
# A subarray is a contiguous subsequence of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0] 
        max_product = curr_max 
        for n in nums[1:]:
            temp_max = max(n, curr_max * n, curr_min * n)
            curr_min = min(n, curr_max * n, curr_min * n)
            curr_max = temp_max
            max_product = max(curr_max, max_product)

        return max_product


# @lc code=end
nums = [2, 3, -2, 4]
nums = [-2, 0, -1]
nums = [2, -5, -2, -4, 3]
s = Solution()
print(s.maxProduct(nums))
