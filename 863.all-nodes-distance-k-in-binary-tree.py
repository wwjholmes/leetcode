#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (57.89%)
# Likes:    3521
# Dislikes: 73
# Total Accepted:    133.6K
# Total Submissions: 229.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
# 
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# 
# 
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
# 
# 
# 
# 
# Note:
# 
# 
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# 
# 
# 
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        queue = deque([(target, 0)])
        visited = {target}
        while queue:
            if queue[0][1] == K:
                break
            node, distance = queue.popleft()
            for n in [node.parent, node.left, node.right]:
                if not n or n in visited:
                    continue
                visited.add(n)
                queue.append([n, distance + 1])

        return [n.val for n, _ in queue]

        
# @lc code=end

