# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (35.99%)
# Likes:    3528
# Dislikes: 642
# Total Accepted:    469.4K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
from typing import List

# directions [i, j]
RIGHT = [1, 0]
DOWN = [0, 1]
LEFT = [-1, 0]
UP = [0, -1]

MOVE = [
    RIGHT, # 0
    DOWN, # 1
    LEFT, # 2
    UP, # 3
]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        m = len(matrix)
        n = len(matrix[0])
        # mark all cell as not visited / False
        visited = [[False for i in range(n)] for j in range(m)]
        direction = 0 # RIGHT
        i = 0
        j = 0

        for w in range(m):
            for h in range(n):
                # push current element
                spiral.append(matrix[j][i])
                visited[j][i] = True
            
                # make a move on 'direction'
                next_i = i + MOVE[direction][0]
                next_j = j + MOVE[direction][1]
            
                if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m or visited[next_j][next_i]:
                    # change direction and re-calculate the next move
                    direction = (direction + 1) % 4
                    next_i = i + MOVE[direction][0]
                    next_j = j + MOVE[direction][1]
                i = next_i
                j = next_j

        return spiral
                
s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))
        
# @lc code=end

