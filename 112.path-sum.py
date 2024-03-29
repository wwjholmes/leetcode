#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (42.41%)
# Likes:    2994
# Dislikes: 597
# Total Accepted:    599.3K
# Total Submissions: 1.4M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3], targetSum = 5
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], targetSum = 0
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# 
# 
#
from collections import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    #     if root == None:
    #         return False

    #     if root.left == None and root.right == None:
    #         return True if targetSum == root.val else False

    #     targetSum -= root.val

    #     if root.left and self.hasPathSum(root.left, targetSum):
    #         return True
    #     elif root.right and self.hasPathSum(root.right, targetSum):
    #         return True

    #     return False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        stack = [(root, targetSum)]
        while stack:
            [node, target] = stack.pop()
            if node.left == None and node.right == None and target == node.val:
                return True
            if node.left:
                stack.append((node.left, target - node.val))
            if node.right:
                stack.append((node.right, target - node.val))
        return False


# @lc code=end
