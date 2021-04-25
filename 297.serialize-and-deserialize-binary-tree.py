#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (49.78%)
# Likes:    4207
# Dislikes: 192
# Total Accepted:    438.1K
# Total Submissions: 869.7K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        stack = [root] if root else []
        pending = []
        valid_node = False
        while stack:
            n = stack.pop(0)
            if n == None:
                serialized.append("null")
                pending.append(None)
                pending.append(None)
            else:
                serialized.append(str(n.val))
                pending.append(n.left)
                pending.append(n.right)
                if n.left or n.right:
                    valid_node = True

            if not stack and valid_node:
                stack = pending
                pending = []
                valid_node = False

        return ','.join(serialized)

            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print('deserialize', data, len(data))
        if not data:
            return []
        vals = data.split(',')
        nodes = [None for _ in range(len(vals))]
        for i in range(len(vals)):
            val = vals[i]
            if val == 'null':
                # empty node
                continue
            node = TreeNode(int(val))
            nodes[i] = node
            parent_idx = (i - 1) // 2
            if parent_idx < 0:
                # root node has no parent
                continue
            parent = nodes[parent_idx]
            if i == 2 * parent_idx + 1:
                parent.left = node
            else:
                parent.right = node
        return nodes[0] if nodes else []
        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)
# t6 = TreeNode(6)
# t7 = TreeNode(7)

# t1.left = t2
# t1.right = t3
# t3.left = t4
# t3.right = t5
# t4.left = t6
# t4.right = t7
# root = t1
# ser = Codec()
# print('serialized:', ser.serialize(root))
# deser = Codec()
# ds = deser.deserialize(ser.serialize(root))
# print(ser.serialize(ds))
 #ans = deser.deserialize(ser.serialize(root))
