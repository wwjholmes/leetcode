#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (34.85%)
# Likes:    1095
# Dislikes: 89
# Total Accepted:    82.8K
# Total Submissions: 236.9K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n' +
  '[[],[1],[1],[2],[],[1],[]]'
#
# Implement the RandomizedCollection class:
# 
# 
# RandomizedCollection() Initializes the RandomizedCollection object.
# bool insert(int val) Inserts an item val into the multiset if not present.
# Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the multiset if present.
# Returns true if the item was present, false otherwise. Note that if val has
# multiple occurrences in the multiset, we only remove one of them.
# int getRandom() Returns a random element from the current multiset of
# elements (it's guaranteed that at least one element exists when this method
# is called). The probability of each element being returned is linearly
# related to the number of same values the multiset contains.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove",
# "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]
# 
# Explanation
# RandomizedCollection randomizedCollection = new RandomizedCollection();
# randomizedCollection.insert(1);   // return True. Inserts 1 to the
# collection. Returns true as the collection did not contain 1.
# randomizedCollection.insert(1);   // return False. Inserts another 1 to the
# collection. Returns false as the collection contained 1. Collection now
# contains [1,1].
# randomizedCollection.insert(2);   // return True. Inserts 2 to the
# collection, returns true. Collection now contains [1,1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 with the
# probability 2/3, and returns 2 with the probability 1/3.
# randomizedCollection.remove(1);   // return True. Removes 1 from the
# collection, returns true. Collection now contains [1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 and 2 both
# equally likely.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= val <= 2^31 - 1
# At most 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is
# called.
# 
# 
# 
# Follow up: Could you implement the functions of the class with each function
# works in average O(1) time?
#
from collections import defaultdict
from random import randrange 
# @lc code=start
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(list)
        self.nums = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        self.store[val].append(len(self.nums) - 1)
        return False if len(self.store[val]) > 1 else True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.store[val]:
            return False

        idx = self.store[val].pop()
        if idx == len(self.nums) - 1:
            self.nums.pop()
        else:
            last_num = self.nums[-1]
            # update [idx] with the last num
            self.nums[idx] = last_num
            
            # update the corresponding index for the lat num
            indexes = self.store[last_num]
            for i, index in enumerate(indexes):
                if index == len(self.nums) - 1:
                    indexes[i] = idx
                    break

            # pop the last element
            self.nums.pop()

        return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        length = len(self.nums)
        return self.nums[randrange(length)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

