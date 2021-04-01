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
        # (A, B), (C, D) + (A, D), (C, B)
        # (E, F), (G, H) + (E, H), (G, F) => Range [E, G], [F, H]

        overlap = False
        if E <= A and A <= G and F <= B and B <= H:
            overlap = True
        elif E <= C and C <= G and F <= D and D <= H:
            overlap = True
        elif E <= A and A <= G and F <= D and D <= H:
            overlap = True
        elif E <= C and C <= G and F <= B and B <= H:
            overlap = True
        
        # case 2: embedding

        if not overlap:
            return (C - A) * (D - B) + (G - E) * (H - F)

        combo_bottom_left_x = min(A, E)
        combo_bottom_left_y = min(B, F)
        combo_top_right_x = max(C, G)
        combo_top_right_y = max(D, H)

        height = combo_top_right_y - combo_bottom_left_y
        width = combo_top_right_x - combo_bottom_left_x

        height_1 = D - B
        width_1 = C - A

        height_2 = H - F
        width_2 = G - E

        return width * height - (width - width_1) * (height - height_2) - (width - width_2) * (height - height_1)


# s = Solution()
# print(s.computeArea(A=-2, B=-2, C=2, D=2, E=-2, F=-2, G=2, H=2))
# print(s.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))


# @lc code=end
