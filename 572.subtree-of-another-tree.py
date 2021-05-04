#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (44.52%)
# Likes:    3399
# Dislikes: 171
# Total Accepted:    310.8K
# Total Submissions: 696.8K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [3,4,5,1,2,null,null,0], subRoot = [4,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def match(a: TreeNode, b: TreeNode) -> bool:
            if not a and not b:
                return True
            if (not a and b) or (a and not b):
                return False
            if a.val != b.val:
                return False
            return match(a.left, b.left) and match(a.right, b.right)

        stack = [root]
        is_subtree = False
        while stack:
            n = stack.pop(0)
            if n.val == subRoot.val and match(n, subRoot):
                is_subtree = True
                break
            n.left and stack.append(n.left)
            n.right and stack.append(n.right)
        return is_subtree

        
# @lc code=end

