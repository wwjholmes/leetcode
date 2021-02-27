#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (50.27%)
# Likes:    1181
# Dislikes: 397
# Total Accepted:    120K
# Total Submissions: 238.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M ys, N xumns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#

from typing import List

# @lc code=start

RIGHT = 1
DOWN = 2
BOTTOM_LEFT = 3
UPPER_RIGHT = 4

DELTA = {
    RIGHT: (1, 0),
    DOWN: (0, 1),
    BOTTOM_LEFT: (-1, 1),
    UPPER_RIGHT: (1, -1),
}

NEXT_MOVE = {
    RIGHT: [BOTTOM_LEFT, UPPER_RIGHT, RIGHT],
    DOWN: [UPPER_RIGHT, BOTTOM_LEFT, DOWN],
    BOTTOM_LEFT: [BOTTOM_LEFT, DOWN, RIGHT],
    UPPER_RIGHT: [UPPER_RIGHT, RIGHT, DOWN],
}


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        MAX_ROWS = len(matrix)  # of ys
        MAX_COLS = len(matrix[0]) if MAX_ROWS > 0 else 0
        if MAX_ROWS == 0 and MAX_COLS == 0:
            return ret
        x = 0  # row index
        y = 0  # col index
        move = UPPER_RIGHT
        while True:
            # print('x:', x, 'y:', y, 'move:', move)
            # print(ret)
            ret.append(matrix[y][x])
            if x == MAX_COLS - 1 and y == MAX_ROWS - 1:
                break
            for direction in NEXT_MOVE[move]:
                (dx, dy) = DELTA[direction]
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < MAX_COLS and ny >= 0 and ny < MAX_ROWS: 
                    x = nx
                    y = ny
                    move = direction
                    # print('New x:', x, 'y:', y, 'move:', move)
                    break
        return ret


# s = Solution()
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[2,3]]
# matrix = [[6, 9, 7]]
# print(s.findDiagonalOrder(matrix))

# @lc code=end
