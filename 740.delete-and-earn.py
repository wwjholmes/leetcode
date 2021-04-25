#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (49.34%)
# Likes:    1486
# Dislikes: 110
# Total Accepted:    51.6K
# Total Submissions: 103K
# Testcase Example:  '[3,4,2]'
#
# Given an array nums of integers, you can perform operations on the array.
# 
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
# 
# You start with 0 points. Return the maximum number of points you can earn by
# applying such operations.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,4,2]
# Output: 6
# Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points.
# 6 total points are earned.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        prev = nums[0]
        count = 1 
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            else:
                pairs.append((prev, prev * count))
                count = 1 
                prev = nums[i]
        pairs.append((prev, prev * count))
        # print(pairs)
        dp = [0 for i in range(len(pairs) + 1)]
        dp[0] = 0
        dp[1] = pairs[0][1]
        for i in range(2, len(pairs) + 1):
            curr = pairs[i-1]
            prev = pairs[i-2]
            if curr[0] == prev[0] + 1:
                dp[i] = max(dp[i-1], dp[i-2] + curr[1])
            else:
                dp[i] = dp[i-1] + curr[1]

        # print(dp)
        return dp[-1]
        

        
# @lc code=end

nums = [2,2,3,3,3,4]
nums = [3,4,2]
nums = [1,1,1,2,4,5,5,5,6]
s = Solution()
print(s.deleteAndEarn(nums))
