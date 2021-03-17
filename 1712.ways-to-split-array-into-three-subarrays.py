#
# @lc app=leetcode id=1712 lang=python3
#
# [1712] Ways to Split Array Into Three Subarrays
#
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/description/
#
# algorithms
# Medium (29.68%)
# Likes:    325
# Dislikes: 39
# Total Accepted:    7.6K
# Total Submissions: 25.7K
# Testcase Example:  '[1,1,1]'
#
# A split of an integer array is good if:
# 
# 
# The array is split into three non-empty contiguous subarrays - named left,
# mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum of the
# elements in mid, and the sum of the elements in mid is less than or equal to
# the sum of the elements in right.
# 
# 
# Given nums, an array of non-negative integers, return the number of good ways
# to split nums. As the number may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1]
# Output: 1
# Explanation: The only good way to split nums is [1] [1] [1].
# 
# Example 2:
# 
# 
# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,2,1]
# Output: 0
# Explanation: There is no good way to split nums.
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^4
# 
#
from typing import List
# @lc code=start
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        presums = {}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            presums[i] = total
        # print(presums)

        count = 0
        for i in range(len(nums) - 2):
            # find first index j that holds [i+1, j] >= left
            left = i + 1
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                mid_sum = presums[mid] - presums[i]
                if mid_sum < presums[i]:
                    # left keeps increasing
                    left = mid + 1
                else:
                    # right keeps decreasing
                    right = mid
            j = left
            if presums[j] - presums[i] < presums[i]:
                break 
            
            # find the last index k that holds [i+1, k] * 2 <= (total - left)
            left = i + 1
            right = len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                mid_sum = presums[mid] - presums[i]
                if 2 * mid_sum <= (total - presums[i]):
                    left = mid
                else:
                    right = mid - 1
            k = min(len(nums) - 2, left)
            if (presums[k] - presums[i]) < presums[i] or (total - presums[k]) < (presums[k] - presums[i]):
                continue

            count += k - j + 1 if k >= j else 0

        return count % (10 ** 9 + 7)


s = Solution()
nums = [3, 2, 1]
nums = [1, 2, 2, 2, 5, 0]
nums = [2,8,10,0,2]
nums = [10,10,5,0,3,8,9]
print(s.waysToSplit(nums))


# @lc code=end
