#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (36.29%)
# Likes:    2767
# Dislikes: 155
# Total Accepted:    166.2K
# Total Submissions: 455.2K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Given the locations and
# heights of all the buildings, return the skyline formed by these buildings
# collectively.
# 
# The geometric information of each building is given in the array buildings
# where buildings[i] = [lefti, righti, heighti]:
# 
# 
# lefti is the x coordinate of the left edge of the i^th building.
# righti is the x coordinate of the right edge of the i^th building.
# heighti is the height of the i^th building.
# 
# 
# You may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# The skyline should be represented as a list of "key points" sorted by their
# x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
# endpoint of some horizontal segment in the skyline except the last point in
# the list, which always has a y-coordinate 0 and is used to mark the skyline's
# termination where the rightmost building ends. Any ground between the
# leftmost and rightmost buildings should be part of the skyline's contour.
# 
# Note: There must be no consecutive horizontal lines of equal height in the
# output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is
# not acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...,[2 3],[4 5],[12 7],...]
# 
# 
# Example 1:
# 
# 
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in
# figure B represent the key points in the output list.
# 
# 
# Example 2:
# 
# 
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1
# buildings is sorted by lefti in non-decreasing order.
# 
# 
#
from typing import List
from heapq import heappush, heappop
# @lc code=start


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # where buildings[i] = [lefti, righti, heighti]:
        # start event: (lefti, -heighti, righti)
        # end event: {righti, 0, 0}
        events = [(lefti, -heighti, righti)
                  for (lefti, righti, heighti) in buildings]
        events += [(righti, 0, 0) for (_, righti, _) in buildings]
        events.sort()
        # print(events)

        res = [(0, 0)]
        max_heap = [(0, float("inf"))]
        for (start, negtive_height, end) in events:
            while max_heap[0][1] <= start:
                heappop(max_heap)

            if negtive_height:
                heappush(max_heap, (negtive_height, end))

            if res[-1][1] != -max_heap[0][0]:
                res.append([start, -max_heap[0][0]])

        return res[1:]


# s = Solution()
# buildings = [[0, 2, 3], [2, 5, 3]]
# buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
# print(s.getSkyline(buildings))

# @lc code=end
