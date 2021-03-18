#
# @lc app=leetcode id=1743 lang=python3
#
# [1743] Restore the Array From Adjacent Pairs
#
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
#
# algorithms
# Medium (62.78%)
# Likes:    217
# Dislikes: 4
# Total Accepted:    9.4K
# Total Submissions: 14.9K
# Testcase Example:  '[[2,1],[3,4],[3,2]]'
#
# There is an integer array nums that consists of n unique elements, but you
# have forgotten it. However, you do remember every pair of adjacent elements
# in nums.
# 
# You are given a 2D integer array adjacentPairs of size n - 1 where each
# adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are
# adjacent in nums.
# 
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1]
# will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1],
# nums[i]]. The pairs can appear in any order.
# 
# Return the original array nums. If there are multiple solutions, return any
# of them.
# 
# 
# Example 1:
# 
# 
# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
# 
# 
# Example 2:
# 
# 
# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
# 
# 
# Example 3:
# 
# 
# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]
# 
# 
# 
# Constraints:
# 
# 
# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 10^5
# -10^5 <= nums[i], ui, vi <= 10^5
# There exists some nums that has adjacentPairs as its pairs.
# 
# 
#
from typing import * 
from collections import *

# @lc code=start


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacents = defaultdict(list)
        for [x, y] in adjacentPairs:
            adjacents[x].append(y)
            adjacents[y].append(x)

        heads = set()
        for k, v in adjacents.items():
            if len(v) == 1:
                heads.add(k)

        def dfs(adjacents: Dict[int, List[int]], restoredArray: List[int], visited: Set[int]) -> List[int]:
            if len(restoredArray) == len(adjacents):
                return True

            tail = restoredArray[-1]
            if tail not in adjacents:
                return False

            for adj in adjacents[tail]:
                if adj in visited:
                    continue
                else:
                    restoredArray.append(adj)
                    visited.add(adj)
                    if dfs(adjacents, restoredArray, visited):
                        return True

            return False

        for head in heads:
            stack = [head]
            if dfs(adjacents, stack, set(stack)):
                return stack

        return []


s = Solution()
adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
adjacentPairs = [[2, 1], [3, 4], [3, 2]]
print(s.restoreArray(adjacentPairs))

# @lc code=end
