#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (42.58%)
# Likes:    3406
# Dislikes: 162
# Total Accepted:    372.2K
# Total Submissions: 871.8K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take labelled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
# bi] this means you must take the course bi before the course ai.
# 
# Given the total number of courses numCourses and a list of the prerequisite
# pairs, return the ordering of courses you should take to finish all courses.
# 
# If there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = {}
        unlock = {}
        for pair in prerequisites:
            ai = pair[0]
            bi = pair[1]
            if ai in dependencies:
                dependencies[ai].add(bi)
            else:
                dependencies[ai] = {bi}
            
            if bi in unlock:
                unlock[bi].add(ai)
            else:
                unlock[bi] = {ai}
        
        # print(dependencies)
        # print(unlock)

        order = []
        while unlock:
            course_unlock = None 
            for u in unlock:
                if u not in dependencies:
                    course_unlock = u 
                    order.append(u)
                    courses = unlock[u]
                    for c in courses:
                        if len(dependencies[c]) == 1:
                            dependencies.pop(c)
                        else:
                            dependencies[c].remove(u)
                    break

            if course_unlock == None:
                return []
            else:
                unlock.pop(course_unlock)
        
        for c in range(numCourses):
            if c not in order:
                order.append(c)

        return order

s = Solution()
numCourses = 1
prerequisites = []
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(numCourses, prerequisites))

        
# @lc code=end

