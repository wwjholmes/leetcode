#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashmap = dict([c, True] for c in allowed)
        count = 0

        for word in words:
            consistent = True 
            for w in word:
                if w not in hashmap:
                   consistent = False 
                   break
            if consistent:
                count += 1

        return count
        
# @lc code=end

