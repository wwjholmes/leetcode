#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/
#
# algorithms
# Hard (56.79%)
# Likes:    621
# Dislikes: 78
# Total Accepted:    35.4K
# Total Submissions: 62.5K
# Testcase Example:  '[6,5,4,3,2,1]\n2'
#
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
# work on the i-th job, you have to finish all the jobs j where 0 <= j < i).
# 
# You have to finish at least one task every day. The difficulty of a job
# schedule is the sum of difficulties of each day of the d days. The difficulty
# of a day is the maximum difficulty of a job done in that day.
# 
# Given an array of integers jobDifficulty and an integer d. The difficulty of
# the i-th job is jobDifficulty[i].
# 
# Return the minimum difficulty of a job schedule. If you cannot find a
# schedule for the jobs return -1.
# 
# 
# Example 1:
# 
# 
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7 
# 
# 
# Example 2:
# 
# 
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you
# cannot find a schedule for the given jobs.
# 
# 
# Example 3:
# 
# 
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.
# 
# 
# Example 4:
# 
# 
# Input: jobDifficulty = [7,1,7,1,7,1], d = 3
# Output: 15
# 
# 
# Example 5:
# 
# 
# Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
# Output: 843
# 
# 
# 
# Constraints:
# 
# 
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10
# 
#
from typing import List
# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # m = d, n = len(jobDifficulty)
        # f(m, n) = min(
        #   f(m-1, n-1) + max(d[n  : n+1]),
        #   f(m-1, n-2) + max(d[n-1: n+1])
        #    ...
        #   f(m-1, 0  ) + max(d[0  : n+1])
        #
        # f (m, n) = inf if m < n
        m = d
        n = len(jobDifficulty)

        f = [[float('inf') for j in range(n)] for i in range(m)]

        for i in range(m):
            max_diff = float('-inf')
            for j in range(n):
                # base case for job schdule with 1 day
                if i == 0:
                    max_diff = max(max_diff, jobDifficulty[j])
                    f[i][j] = max_diff
                else:
                    # other cases when d > 1
                    min_diff = float('inf')
                    max_diff = float('-inf')
                    for k in range(0, j):
                        max_diff = max(max_diff, jobDifficulty[j-k])
                        diff = f[i-1][j-k-1] + max(max_diff, jobDifficulty[j-k])
                        min_diff = min(min_diff, diff)
                    f[i][j] = float('inf') if i > j else min_diff
        # print(f)
        return f[m-1][n-1] if f[m-1][n-1] != float('inf') else -1

                

# @lc code=end
# s = Solution()
# jobDifficulty = [1,1,1]
# d = 3
# jobDifficulty = [6,5,4,3,2,1]
# d = 2
# jobDifficulty = [7,1,7,1,7,1]
# d = 3
# jobDifficulty = [9,9,9]
# d = 4
# jobDifficulty = [11,111,22,222,33,333,44,444]
# d = 6
# print(s.minDifficulty(jobDifficulty, d))
