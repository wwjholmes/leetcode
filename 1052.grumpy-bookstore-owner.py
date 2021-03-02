#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#
# https://leetcode.com/problems/grumpy-bookstore-owner/description/
#
# algorithms
# Medium (55.82%)
# Likes:    674
# Dislikes: 65
# Total Accepted:    36K
# Total Submissions: 64.5K
# Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
#
# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and
# all those customers leave after the end of that minute.
# 
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
# grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
# bookstore owner is grumpy, the customers of that minute are not satisfied,
# otherwise they are satisfied.
# 
# The bookstore owner knows a secret technique to keep themselves not grumpy
# for X minutes straight, but can only use it once.
# 
# Return the maximum number of customers that can be satisfied throughout the
# day.
# 
# 
# 
# Example 1:
# 
# 
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3
# minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5
# = 16.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1
# 
#

from typing import List

# @lc code=start


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total = 0
        max_delta = 0
        shift_delta = 0
        for i in range(len(customers)):
            total += customers[i] if grumpy[i] == 0 else 0

            if i < X:
                delta = customers[i] if grumpy[i] == 1 else 0
                shift_delta += delta
                max_delta = max(max_delta, shift_delta)
                # print(shift_delta, max_delta)
            else:
                add = customers[i] if grumpy[i] == 1 else 0
                remove = customers[i - X] if grumpy[i - X] == 1 else 0
                shift_delta += add - remove
                max_delta = max(max_delta, shift_delta)
                # print(shift_delta, max_delta)

        # print(total, max_delta)
        return total + max_delta


s = Solution()
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
print(s.maxSatisfied(customers, grumpy, X))

# @lc code=end
