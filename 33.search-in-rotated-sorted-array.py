#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (35.87%)
# Likes:    7336
# Dislikes: 643
# Total Accepted:    958.6K
# Total Submissions: 2.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
# [4,5,6,7,0,1,2].
# 
# Given the array nums after the rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
# 
# Follow up: Can you achieve this in O(log n) time complexity?
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot index
        def findPivot(left: int, right: int) -> int:
            if nums[left] <= nums[right]:
                return left
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                return findPivot(mid + 1, right)
            elif nums[mid] <= nums[right]:
                return findPivot(left, mid)

        length = len(nums)
        left = findPivot(0, length -1)
        right = left + length -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid % length] >= target:
                right = mid
            else:
                left = mid + 1

        return left % length if nums[left % length] == target else -1





            

        
# @lc code=end

# s = Solution()
# nums = [4,5,6,7,0,1,2]
# target = 3 
# nums = [1]
# target = 0
# print(s.search(nums, target))
