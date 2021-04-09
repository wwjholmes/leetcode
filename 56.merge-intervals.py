#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (41.03%)
# Likes:    6968
# Dislikes: 375
# Total Accepted:    858.7K
# Total Submissions: 2.1M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

from typing import List
# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by their start value
        intervals.sort()
        # invariant: all intervals in merged are sorted and non-overlapping
        merged = []
        for curr in intervals:
            if not merged:
                merged.append(curr)
            else:
                prev = merged[-1]
                if curr[0] > prev[1]:
                    # no overlap
                    merged.append(curr)
                else:
                    merged.pop()
                    merged.append([prev[0], max(prev[1], curr[1])])
        return merged

# @lc code=end


# s = Solution()
# intervals = [[1, 4], [4, 5]]
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(s.merge(intervals))
