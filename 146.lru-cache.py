#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (35.75%)
# Likes:    8151
# Dislikes: 334
# Total Accepted:    735.9K
# Total Submissions: 2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# Follow up:
# Could you do get and put in O(1) time complexity?
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 3000
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to get and put.
# 
# 
#
from collections import defaultdict

# @lc code=start


class LRUCache:

    # internal Node structure
    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    # internal doublely linked list
    class DoubleLinkedList:
        def __init__(self):
            self.head = LRUCache.Node(0, 0)
            self.tail = LRUCache.Node(0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head

        def removeFirst(self):
            if self.head.next != self.tail:
                first = self.head.next
                self.head.next = first.next
                first.next.prev = self.head
                return first

        def remove(self, node):
            # remove node from list
            p_node = node.prev
            n_node = node.next
            p_node.next = n_node
            n_node.prev = p_node

        def push(self, node):
            # insert node right before self.tail
            p_node = self.tail.prev
            p_node.next = node
            node.prev = p_node
            node.next = self.tail
            self.tail.prev = node

        def printList(self):
            n = self.head.next
            stack = []
            while n != self.tail:
                stack.append(n.key)
                n = n.next
            print(stack)


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.dlist = self.DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.dict[key]

        # remove node from list and re-insert at the end
        self.dlist.remove(node)
        self.dlist.push(node)
        # print('get', key)
        # self.dlist.printList()
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            # update Node value
            node.val = value
            self.dlist.remove(node)
            self.dlist.push(node)
        else:
            if len(self.dict) == self.capacity:
                # remove node from both dict and list
                first_node = self.dlist.removeFirst()
                del self.dict[first_node.key]
                # print('del', first_node.key, first_node.val)

            node = self.Node(key, value)
            self.dict[key] = node
            self.dlist.push(node)
        # print('put', key, value)
        # self.dlist.printList()


# Your LRUCache object will be instantiated and called as such:
# ops = ["LRUCache", "put", "put", "get",
#        "put", "get", "put", "get", "get", "get"]
# values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# stack = []
# for i, op in enumerate(ops):
#     if op == "LRUCache":
#         [capacity] = values[i]
#         obj = LRUCache(2)
#         stack.append(None)
#     elif op == "put":
#         [key, val] = values[i]
#         obj.put(key, val)
#         stack.append(None)
#     elif op == "get":
#         [key] = values[i]
#         val = obj.get(key)
#         stack.append(val)
# print(stack)


# @lc code=end
