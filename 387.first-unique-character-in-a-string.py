#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (53.76%)
# Likes:    2793
# Dislikes: 139
# Total Accepted:    708.3K
# Total Submissions: 1.3M
# Testcase Example:  '"leetcode"'
#
# Given a string s, return the first non-repeating character in it and return
# its index. If it does not exist, return -1.
# 
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
# 
# 
#
from collections import defaultdict
# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        stats = defaultdict(int)
        for c in s:
            stats[c] = stats[c] + 1

        for i in range(len(s)):
            if stats[s[i]] == 1:
                return i

        return -1

# @lc code=end
