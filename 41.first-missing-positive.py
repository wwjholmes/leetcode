#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (33.68%)
# Likes:    5390
# Dislikes: 953
# Total Accepted:    458.3K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array nums, find the smallest missing positive
# integer.
# 
# 
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 300
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you implement an algorithm that runs in O(n) time and uses
# constant extra space?
# 
#
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        missing_one = True
        for i in range(n):
            if nums[i] == 1:
                missing_one = False
            elif nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # if 1 is the first missing positive number
        if missing_one:
            return 1
        
        # flip the corresponding nums[index] to nagetive
        for i in range(n):
            index = abs(nums[i]) % n
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # return the first number/index which is still positive
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # if all numbers [1..n] are in nums, then 
        if nums[0] > 0:
            return n
        else:
            return n + 1


s = Solution()
nums = [7, 8, 9, 11, 12]
nums = [1, 2, 0]
nums = [3, 4, -1, 1]
nums = [1, 2]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,23,20]
print(s.firstMissingPositive(nums))

        
        
# @lc code=end

