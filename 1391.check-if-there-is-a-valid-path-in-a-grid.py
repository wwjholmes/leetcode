#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#
from copy import copy, deepcopy
from typing import List

# @lc code=start


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = [[False for y in grid[0]]for x in grid]
        first = grid[0][0]
        if first == 1:
            return self.moveToNext(0, 0, 2, grid, visited) or self.moveToNext(0, 0, 4, grid, visited)
        if first == 2:
            return self.moveToNext(0, 0, 1, grid, visited) or self.moveToNext(0, 0, 3, grid, visited)
        if first == 3:
            return self.moveToNext(0, 0, 2, grid, visited) or self.moveToNext(0, 0, 1, grid, visited)
        if first == 4:
            return self.moveToNext(0, 0, 1, grid, visited) or self.moveToNext(0, 0, 4, grid, visited)
        if first == 5:
            return self.moveToNext(0, 0, 2, grid, visited) or self.moveToNext(0, 0, 3, grid, visited)
        if first == 6:
            return self.moveToNext(0, 0, 3, grid, visited) or self.moveToNext(0, 0, 4, grid, visited)

    def moveToNext(self, i: int, j: int, direction: int, grid: List[List[int]], visited: List[List[bool]]) -> bool:
        n = len(grid)  # height of grid
        m = len(grid[0])  # width of grid

        # reach the bottom-right cell
        if i == m - 1 and j == n - 1:
            if grid[j][i] == 1:
                return direction == 2 or direction == 4
            if grid[j][i] == 2:
                return direction == 1 or direction == 3
            if grid[j][i] == 3:
                return direction == 1 or direction == 2
            if grid[j][i] == 4:
                return direction == 1 or direction == 4
            if grid[j][i] == 5:
                return direction == 2 or direction == 3
            if grid[j][i] == 6:
                return direction == 3 or direction == 4
            return False 

        # out of grid
        if i < 0 or i >= m:
            return False
        if j < 0 or j >= n:
            return False

        # if current cell already being marked as visited, return False
        if visited[j][i]:
            return False

        # mark current cell as visited
        visited[j][i] = True

        cell = grid[j][i]
        if cell == 1:
           if direction == 4 and self.moveToNext(i - 1, j, 4, grid, visited):
               return True
           elif direction == 2 and self.moveToNext(i + 1, j, 2, grid, visited):
               return True
        elif cell == 2:
           if direction == 1 and self.moveToNext(i, j - 1, 1, grid, visited):
               return True
           elif direction == 3 and self.moveToNext(i, j + 1, 3, grid, visited):
               return True
        elif cell == 3:
           if direction == 1 and self.moveToNext(i - 1, j, 4, grid, visited):
               return True
           elif direction == 2 and self.moveToNext(i, j + 1, 3,  grid, visited):
               return True
        elif cell == 4:
           if direction == 1 and self.moveToNext(i + 1, j, 2, grid, visited):
               return True
           elif direction == 4 and self.moveToNext(i, j + 1, 3, grid, visited):
               return True
        elif cell == 5:
           if direction == 3 and self.moveToNext(i - 1, j, 4, grid, visited):
               return True
           elif direction == 2 and self.moveToNext(i, j - 1, 1, grid, visited):
               return True
        elif cell == 6:
           if direction == 3 and self.moveToNext(i + 1, j, 2, grid, visited):
               return True
           elif direction == 4 and self.moveToNext(i, j - 1, 1, grid, visited):
               return True

        # mark current cell as un-visited before return
        visited[j][i] = False 
        return False

# @lc code=end
