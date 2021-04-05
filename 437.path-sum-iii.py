#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (48.12%)
# Likes:    4965
# Dislikes: 322
# Total Accepted:    262.8K
# Total Submissions: 544.3K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def countPathSum(root: TreeNode, target: int, started: bool) -> int:
            count = 0
            if root.val == target:
                count += 1

            if root.left:
                if not started:
                    count += countPathSum(root.left, target, False)
                count += countPathSum(root.left, target - root.val, True)

            if root.right:
                if not started:
                    count += countPathSum(root.right, target, False)
                count += countPathSum(root.right, target - root.val, True)

            return count
        if root == None:
            return 0

        return countPathSum(root, sum, False)


# @lc code=end
