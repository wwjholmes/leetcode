#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (42.66%)
# Likes:    6903
# Dislikes: 349
# Total Accepted:    856.9K
# Total Submissions: 2M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
# 
# 
#
from __future__ import annotations
from typing import List
from heapq import heapify, heappop, heappush
# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: ListNode) -> bool:
        return self.val == other.val

    def __ne__(self, other: ListNode) -> bool:
        return self.val != other.val

    def __gt__(self, other: ListNode) -> bool:
        return self.val > other.val

    def __lt__(self, other: ListNode) -> bool:
        return self.val < other.val

    def __ge__(self, other: ListNode) -> bool:
        return self.val >= other.val

    def __le__(self, other: ListNode) -> bool:
        return self.val <= other.val

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> List[ListNode]:
        count = 0
        filtered = []
        for node in lists:
            if not node:
                continue
            filtered.append((node.val, count, node))
            count += 1
        heapify(filtered)
        head = ListNode(0)
        curr_node = head
        while filtered:
            [val, _, list_node] = heappop(filtered)
            curr_node.next = list_node
            curr_node = list_node
            next_node = list_node.next
            if next_node:
                count += 1
                heappush(filtered, (next_node.val, count, next_node))
        return head.next

# @lc code=end


# s = Solution()
# lists = []
# lists = [ListNode(1), ListNode(3), ListNode(2)]
# for n in s.mergeKLists(lists):
#     print(n)
