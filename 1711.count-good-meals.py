#
# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
#
# https://leetcode.com/problems/count-good-meals/description/
#
# algorithms
# Medium (26.04%)
# Likes:    194
# Dislikes: 133
# Total Accepted:    11.5K
# Total Submissions: 44.2K
# Testcase Example:  '[1,3,5,7,9]'
#
# A good meal is a meal that contains exactly two different food items with a
# sum of deliciousness equal to a power of two.
# 
# You can pick any two different foods to make a good meal.
# 
# Given an array of integers deliciousness where deliciousness[i] is the
# deliciousness of the i^​​​​​​th​​​​​​​​ item of food, return the number of
# different good meals you can make from this list modulo 10^9 + 7.
# 
# Note that items with different indices are considered different even if they
# have the same deliciousness value.
# 
# 
# Example 1:
# 
# 
# Input: deliciousness = [1,3,5,7,9]
# Output: 4
# Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
# Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
# 
# 
# Example 2:
# 
# 
# Input: deliciousness = [1,1,1,3,3,3,7]
# Output: 15
# Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and
# (1,7) with 3 ways.
# 
# 
# Constraints:
# 
# 
# 1 <= deliciousness.length <= 10^5
# 0 <= deliciousness[i] <= 2^20
# 
# 
#
from typing import List
import math

# @lc code=start

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        for i in range(len(deliciousness)):
            t = deliciousness[i]
            count[t] = 1 if t not in count else count[t] + 1

        total = 0
        for k in count.keys():
            if k == 0:
                continue

            expo = math.ceil(math.log(k, 2))
            target = 2 ** expo
            # print(k, target)

            if target == k:
                total += int(count[k] * (count[k] - 1) / 2)

            if target - k in count:
                total += count[target - k] * count[k]

        return total % (10 ** 9 + 7)


s = Solution()
deliciousness = [1, 3, 5, 7, 9]
deliciousness = [1, 1, 1, 3, 3, 3, 7]
deliciousness = [149, 107, 1, 63, 0, 1, 6867, 1325,
                 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]
print(s.countPairs(deliciousness))

# @lc code=end
