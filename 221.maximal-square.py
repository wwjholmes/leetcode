#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (39.19%)
# Likes:    4459
# Dislikes: 105
# Total Accepted:    350.4K
# Total Submissions: 884.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# 
# 
#
from typing import List
# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # F(m, n) and S(m, n) is the length of the maximum square
        # F(m, n) = max(F(m, n-1), F(m-1, n), S(m, n), K(m, n))
        # S(m, n) = S(m-1, n-1) + 1 if all 1s else 0
        # K(m, n) = 1 if matrix[m, n] == '1' else 0

        m = len(matrix)
        n = len(matrix[0])
        F = [[0 for j in range(n)]for i in range(m)]
        S = [[0 for j in range(n)]for i in range(m)]
        # fill base cases e.g. f(0, n), f(m, 0)
        F[0][0] = int(matrix[0][0])
        S[0][0] = int(matrix[0][0])

        for i in range(1, m):
            F[i][0] = 1 if matrix[i][0] == '1' or F[i-1][0] else 0
            S[i][0] = 1 if matrix[i][0] == '1' else 0

        for j in range(1, n):
            F[0][j] = 1 if matrix[0][j] == '1' or F[0][j-1] else 0
            S[0][j] = 1 if matrix[0][j] == '1' else 0

        for i in range(1, m):
            for j in range(1, n):
                if S[i-1][j-1] == 0 and matrix[i][j] == '0':
                    S[i][j] = 0
                elif S[i-1][j-1] == 0 and matrix[i][j] == '1':
                    S[i][j] = 1
                elif S[i-1][j-1] > 0:
                    count = 0
                    for k in range(S[i-1][j-1] + 1):
                        if matrix[i-k][j] == '1' and matrix[i][j-k] == '1':
                            count += 1
                        else:
                            break
                    S[i][j] = count
                else:
                    raise Exception(
                        'invalid result in S[m][m], i = ', i, ' j = ', j)
                F[i][j] = max(F[i][j-1], F[i-1][j], S[i][j], int(matrix[i][j]))
        # print(F)
        # print(S)
        return F[-1][-1] * F[-1][-1]


# @lc code=end

s = Solution()
matrix = [["0","1"],["1","0"]]
matrix = [["1","0"]]
matrix = [["1"]]
matrix = [["0","0"]]
matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
print(s.maximalSquare(matrix))
