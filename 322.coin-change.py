#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (37.20%)
# Likes:    6661
# Dislikes: 193
# Total Accepted:    624.2K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: coins = [1], amount = 1
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: coins = [1], amount = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#
from typing import List
# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for _ in range(amount + 1)]
        dp[0] = [True, 0]

        def minCoinChange(amount: int, dp: List) -> List:
            if dp[amount] != None:
                return dp[amount]

            min_count = -1
            for c in coins:
                if c == amount:
                    min_count = 1
                    break
                elif c < amount:
                    [is_possible, count] = minCoinChange(amount - c, dp)
                    if is_possible:
                        min_count = (count + 1) if min_count == - \
                            1 else min(min_count, count + 1)
            ret = [True, min_count] if min_count > 0 else [False, -1]
            dp[amount] = ret
            return ret

        return minCoinChange(amount, dp)[1]


# @lc code=end

# s = Solution()
# coins = [1]
# amount = 2
# coins = [1]
# amount = 1
# coins = [1]
# amount = 0
# coins = [2]
# amount = 3
# coins = [1, 2, 5]
# amount = 11
# print(s.coinChange(coins, amount))
# 