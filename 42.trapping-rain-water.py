#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.17%)
# Likes:    10301
# Dislikes: 155
# Total Accepted:    694.7K
# Total Submissions: 1.4M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#
from typing import List
# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        current = 0 if left_max <= right_max else -1
        trapped_water = 0

        while left <= right:
            h = height[current]
            if left_max <= right_max:
                if h < left_max:
                    trapped_water += left_max - h
                left_max = max(left_max, h)
            else:
                if h < right_max:
                    trapped_water += right_max - h
                right_max = max(right_max, h)

            # move to the next position
            if left_max <= right_max:
                left += 1
                current = left
            else:
                right -= 1
                current = right

        return trapped_water


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
height = [4,2,3]
print(s.trap(height))


# @lc code=end
