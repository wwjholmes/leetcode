#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (38.21%)
# Likes:    530
# Dislikes: 869
# Total Accepted:    118K
# Total Submissions: 307.9K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the
# total area covered by the two rectangles.
# 
# The first rectangle is defined by its bottom-left corner (A, B) and its
# top-right corner (C, D).
# 
# The second rectangle is defined by its bottom-left corner (E, F) and its
# top-right corner (G, H).
# 
# 
# Example 1:
# 
# 
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# 
# 
# Example 2:
# 
# 
# Input: A = -2, B = -2, C = 2, D = 2, E = -2, F = -2, G = 2, H = 2
# Output: 16
# 
# 
# 
# Constraints:
# 
# 
# -10^4 <= A, B, C, D, E, F, G, H <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # (A, B), (C, D)
        # (E, F), (G, H)
        min_x = min(A, E)
        min_y = min(B, F)
        max_x = max(C, G)
        max_y = max(D, H)

        height = max_y - min_y
        width = max_x - min_x

        height_one = D - B
        width_one = C - A

        height_two = H - F
        width_two = G - E
        sum_area = (C - A) * (D - B) + (G - E) * (H - F)
        if height < height_one + height_two and width < width_one + width_two:
            return sum_area - (width_one + width_two - width) * (height_one + height_two - height)
        else:
            return sum_area


# s = Solution()
# print(s.computeArea(A=-2, B=-2, C=2, D=2, E=-2, F=-2, G=2, H=2))
# print(s.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))
# print(s.computeArea(A=-2, B=-2, C=2, D=2, E=-1, F=-1, G=1, H=1))
# print(s.computeArea(A=-3, B=-3, C=3, D=-1, E=-2, F=-2, G=2, H=2))


# @lc code=end
