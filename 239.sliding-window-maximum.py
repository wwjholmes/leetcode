#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (44.63%)
# Likes:    5414
# Dislikes: 226
# Total Accepted:    379.4K
# Total Submissions: 849K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# 
# 
# Example 4:
# 
# 
# Input: nums = [9,11], k = 2
# Output: [11]
# 
# 
# Example 5:
# 
# 
# Input: nums = [4,-2], k = 2
# Output: [4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        window = []
        def cleanupWindow(idx: int):
            if window and idx - k == window[0]:
                window.pop(0)

            while window and nums[idx] >= nums[window[-1]]:
                window.pop()
            # print(idx, window)

        for i in range(len(nums)):
            cleanupWindow(i)
            window.append(i)
            if i >= k -1:
                max_nums.append(nums[window[0]])

        return max_nums

# s = Solution()
# nums = [1]
# k = 1
# nums = [1,-1]
# k = 1
# nums = [9,11]
# k = 2
# nums = [4,-2]
# k = 2
# print(s.maxSlidingWindow(nums, k))


        
# @lc code=end

