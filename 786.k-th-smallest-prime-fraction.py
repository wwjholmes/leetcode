#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#
# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
#
# algorithms
# Hard (42.55%)
# Likes:    491
# Dislikes: 29
# Total Accepted:    17.5K
# Total Submissions: 41K
# Testcase Example:  '[1,2,3,5]\n3'
#
# You are given a sorted integer array arr containing 1 and prime numbers,
# where all the integers of arr are unique. You are also given an integer k.
# 
# For every i and j where 0 <= i < j < arr.length, we consider the fraction
# arr[i] / arr[j].
# 
# Return the k^th smallest fraction considered. Return your answer as an array
# of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,7], k = 1
# Output: [1,7]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 10^4
# arr[0] == 1
# arr[i] is a prime number for i > 0.
# All the numbers of arr are unique and sorted in strictly increasing
# order.
# 1 <= k <= arr.length * (arr.length - 1) / 2
# 
# 
#
import heapq
from typing import List
from functools import *

# @lc code=start


class Solution:
    def compare(self, x, y):
        (a, b) = x
        (c, d) = y
        return 1 if a * d > b * c else -1

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                h.append((arr[i], arr[j]))

        k_arr = heapq.nsmallest(k, h, cmp_to_key(self.compare))
        (x, y) = k_arr[-1]
        return [x, y]


# @lc code=end

s = Solution()
arr = [1, 7]
k = 1
arr = [1, 2, 3, 5]
k = 3
print(s.kthSmallestPrimeFraction(arr, k))
