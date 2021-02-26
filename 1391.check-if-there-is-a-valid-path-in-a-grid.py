#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#
from copy import copy, deepcopy
from typing import List

# @lc code=start


class Solution:
    STREET_1: int = 1
    STREET_2: int = 2
    STREET_3: int = 3
    STREET_4: int = 4
    STREET_5: int = 5
    STREET_6: int = 6

    directions = {
        # option1: (row, col), option2: (row, col)
        STREET_1: [(0, -1), (0, 1)],
        STREET_2: [(-1, 0), (1, 0)],
        STREET_3: [(1, 0), (0, -1)],
        STREET_4: [(1, 0), (0, 1)],
        STREET_5: [(-1, 0), (0, -1)],
        STREET_6: [(-1, 0), (0, 1)],
    }

    connected = {
        STREET_1:
        {
            0: [STREET_1, STREET_4, STREET_6],
            1: [STREET_1, STREET_3, STREET_5],
        },
        STREET_2:
        {
            0: [STREET_2, STREET_3, STREET_4],
            1: [STREET_2, STREET_5, STREET_6],
        },
        STREET_3:
        {
            0: [STREET_2, STREET_5, STREET_6],
            1: [STREET_1, STREET_3, STREET_5],
        },
        STREET_4:
        {
            0: [STREET_2, STREET_5, STREET_6],
            1: [STREET_1, STREET_3, STREET_5],
        },
        STREET_5:
        {
            0: [STREET_2, STREET_3, STREET_4],
            1: [STREET_1, STREET_4, STREET_6],
        },
        STREET_6:
        {
            0: [STREET_2, STREET_3, STREET_4],
            1: [STREET_1, STREET_3, STREET_5],
        },
    }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = [[False for y in grid[0]]for x in grid]
        m = len(grid)
        n = len(grid[0])

        stack = [(0, 0)]
        while stack:
            (row, col) = stack.pop()
            # print('pop:', (row, col))
            if row == m - 1 and col == n - 1:
                return True

            street = grid[row][col]
            visited[row][col] = True

            for idx, (dx, dy) in enumerate(self.directions[street]):
                nx = row + dx
                ny = col + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if visited[nx][ny]:
                    continue

                if grid[nx][ny] in self.connected[street][idx]:
                    # print('push:', (nx, ny))
                    stack.append((nx, ny))

        return False

# s = Solution()
# grid = [[1, 1, 2]]
# grid = [[1, 2, 1], [1, 2, 1]]
# grid = [[1,1,1,1,1,1,3]]
# grid = [[2,4,3],[6,5,2]]
# print(s.hasValidPath(grid))

# @lc code=end
