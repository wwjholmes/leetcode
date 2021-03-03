#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/
#
# algorithms
# Medium (81.72%)
# Likes:    850
# Dislikes: 148
# Total Accepted:    52.1K
# Total Submissions: 63.8K
# Testcase Example:  '[[3,3,1,1],[2,2,1,2],[1,1,1,2]]'
#
# A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right
# direction until reaching the matrix's end. For example, the matrix diagonal
# starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells
# mat[2][0], mat[3][1], and mat[4][2].
# 
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
# order and return the resulting matrix.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# 
# 
# Example 2:
# 
# 
# Input: mat =
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output:
# [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)  # num of rows
        n = len(mat[0])  # num of cols

        head_cells = [(0, x) for x in range(m)]
        head_cells += [(y, 0) for y in range(1, n)]
        # print(head_cells)

        # use simple bubble sort
        for (i, j) in head_cells:
            while i < n and j < m:
                ii = i
                jj = j
                diagonal = []
                while ii < n and jj < m:
                    diagonal.append(mat[jj][ii])
                    ii += 1
                    jj += 1

                ii -= 1
                jj -= 1

                diagonal = sorted(diagonal)

                while ii >= i and jj >= j:
                    mat[jj][ii] = diagonal.pop()
                    ii -= 1
                    jj -= 1

                i += 1
                j += 1
        return mat


# s = Solution()
# mat = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [
    # 75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
# mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
# s.diagonalSort(mat)
# print(mat)

# @lc code=end
