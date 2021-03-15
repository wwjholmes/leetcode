#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (49.07%)
# Likes:    7894
# Dislikes: 240
# Total Accepted:    987.9K
# Total Submissions: 2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#
from typing import List
# @lc code=start
# MOVE [x, y]
# x - vertical, row index
# y - horizontal, column index 

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

DIRECTIONS = [
    UP,
    DOWN,
    LEFT,
    RIGHT,
]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited= [[False for y in range(n)] for x in range(m)]
        stack = [[0, 0]]
        islands = 0
        while stack:
            pos = stack.pop(0)
            if visited[pos[0]][pos[1]]:
                continue
            if grid[pos[0]][pos[1]] == "1":
                islands += 1
            self.dfs(grid, visited, stack, pos)
        return islands

    def dfs(self, grid: List[List[str]], visited: List[List[bool]], stack: List[List[int]], pos: List[int]):
        target = grid[pos[0]][pos[1]]
        visited[pos[0]][pos[1]] = True
        m = len(grid)
        n = len(grid[0])
        for d in DIRECTIONS:
            nx = pos[0] + d[0]
            ny = pos[1] + d[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif visited[nx][ny]:
                continue
            else:
                if grid[nx][ny] == target:
                    self.dfs(grid, visited, stack, [nx, ny])
                else:
                    stack.append([nx, ny])


s = Solution()
g = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(s.numIslands(g))




        
# @lc code=end

