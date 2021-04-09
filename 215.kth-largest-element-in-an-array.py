#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (58.40%)
# Likes:    5425
# Dislikes: 351
# Total Accepted:    870.7K
# Total Submissions: 1.5M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# 
# 
#
from heapq import *
from typing import List
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        heapify(queue)
        for n in nums:
            if len(queue) < k:
                heappush(queue, n)
            else:
                if n > queue[0]:
                    heappop(queue)
                    heappush(queue, n)
            # print(n, queue)

        # return the kth element
        return queue[0]

        
# @lc code=end

# s = Solution()
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
# nums = [3,2,1,5,6,4]
# k = 2
# print(s.findKthLargest(nums, k))
