#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (50.09%)
# Likes:    3377
# Dislikes: 127
# Total Accepted:    506.2K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        zigzag = [[root.val]]
        next = []
        left_to_right = False
        while stack:
            for n in stack:
                n.left and next.append(n.left)
                n.right and next.append(n.right)

            if not next:
                break
            # add current stack to zigzag
            if left_to_right:
                zigzag.append([n.val for n in next])
            else:
                zigzag.append([n.val for n in next[::-1]])

            stack = next
            next = []
            left_to_right = not left_to_right
        return zigzag
                    



        
# @lc code=end

