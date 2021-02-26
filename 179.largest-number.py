# @before-stub-for-debug-begin
from python3problem179 import *
from typing import *
from functools import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start

def custom_compare(x: str, y: str) -> int:
    if x == y :
        return 0
    elif x + y > y + x : 
        return 1
    else:
        return -1 


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = ''.join(sorted(map(str, nums), key=cmp_to_key(custom_compare), reverse=True))
        return s[:-1].lstrip('0') + s[-1]
                
 # @lc code=end

