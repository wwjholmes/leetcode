#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (54.43%)
# Likes:    1228
# Dislikes: 916
# Total Accepted:    103.7K
# Total Submissions: 190.4K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# 
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
# 
# 
# 
# Constraints:
# 
# 
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # (start index, end index, degree)
        h = {}
        max_degree = 1 
        max_nums = {nums[0]} 
        for index, x in enumerate(nums):
            if x in h:
                (start, end, degree) = h[x]
                degree += 1
                h[x] = (start, index, degree)

                if degree  >  max_degree:
                    max_degree = degree
                    max_nums = {x}
                if degree == max_degree:
                    max_nums.add(x)
            else:
                h[x] = (index, index, 1)
        # print(h)
        # print(max_nums)
        
        min_length =  len(nums)
        for x in max_nums:
            (start, end, _) = h[x]
            length = end - start + 1
            min_length = length if length < min_length else min_length

        return min_length
            

s = Solution()
nums = [1, 2, 2, 3, 1, 4, 2]
print(s.findShortestSubArray(nums))


        
# @lc code=end

