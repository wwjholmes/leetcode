#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
#
# algorithms
# Hard (47.48%)
# Likes:    1146
# Dislikes: 12
# Total Accepted:    35.5K
# Total Submissions: 74.8K
# Testcase Example:  '[1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]'
#
# We have n jobs, where every job is scheduled to be done from startTime[i] to
# endTime[i], obtaining a profit of profit[i].
# 
# You're given the startTime, endTime and profit arrays, return the maximum
# profit you can take such that there are no two jobs in the subset with
# overlapping time range.
# 
# If you choose a job that ends at time X you will be able to start another job
# that starts at time X.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# 
# 
# Example 2:
# 
# ⁠
# 
# 
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit =
# [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4
# 
# 
#
from bisect import bisect_left
from typing import List
from collections import defaultdict
# @lc code=start

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if len(startTime) == 0:
            return 0

        # sort jobs according startTime
        jobs = [(startTime[i], endTime[i], profit[i])
                for i in range(len(startTime))]
        jobs.sort()
        
        optimals = defaultdict(int)

        def maxProfit(current: int) -> int:
            if current == len(jobs) - 1:
                # last job in the array
                return jobs[current][2]
            if current in optimals:
                return optimals[current]

            # case 1: optimal solution contains current job
            current_profit = jobs[current][2]
            next_index = bisect_left(
                jobs, (jobs[current][1], jobs[current][1], 0), current + 1)
            next_profit = maxProfit(
                next_index) if next_index < len(jobs) else 0
            max_profit = current_profit + next_profit

            # case 2: optimal solution doesn't contain currentjob
            max_profit_without_current = maxProfit(current + 1)

            optimals[current] = max(max_profit, max_profit_without_current)
            return optimals[current]

        return maxProfit(0)


# s = Solution()
# startTime = [1, 1, 1]
# endTime = [2, 3, 4]
# profit = [5, 6, 4]
# startTime = [1, 2, 3, 4, 6]
# endTime = [3, 5, 10, 6, 9]
# profit = [20, 20, 100, 70, 60]
# startTime = [1,2,3,3]
# endTime = [3,4,5,6]
# profit = [50,10,40,70]
# startTime = [4,2,4,8,2]
# endTime = [5,5,5,10,8]
# profit = [1, 2, 8, 10, 4]
# startTime = [631,919,696,968,618,133,263,517,265,290,741,646,534,605,978,584,937,37,666,446,264,58,461,648,382,783,719,958,247,837,547,978,169,172,545,326,720,232,121,335,575,496,701,662,201,641,158,976,658,888,645,338,401,627,803,716,139,243,382,592,287,743,683,162,220,871,957,694,108,318,390,416,855,922,293,116,574,759,50,690,314,424,607,894,520,972,85,214,118,992,197,865,826,160,19,583,520,585,268,872]
# endTime = [811,960,887,986,685,440,339,709,682,510,897,896,588,906,980,604,984,676,788,748,814,207,852,905,478,880,732,986,327,864,739,990,221,354,594,763,962,273,139,416,852,887,809,959,718,919,175,994,897,987,651,530,939,819,807,874,956,651,809,952,442,861,990,535,732,926,965,900,195,595,492,432,950,963,857,280,712,794,751,732,754,531,710,958,694,982,884,352,729,996,253,947,940,268,442,763,963,862,760,884]
# profit = [7,25,35,83,75,89,61,23,28,97,43,100,92,29,97,44,52,55,91,18,27,7,34,41,11,12,20,89,50,96,80,36,90,79,91,18,12,50,95,32,78,66,17,59,60,39,18,75,73,75,60,49,75,86,67,10,76,6,40,81,35,93,29,96,94,92,99,3,76,88,97,64,79,39,5,81,46,82,82,86,43,54,36,35,90,26,65,59,22,44,84,14,97,99,81,35,41,15,82,30]

# print(s.jobScheduling(startTime, endTime, profit))

# @lc code=end
