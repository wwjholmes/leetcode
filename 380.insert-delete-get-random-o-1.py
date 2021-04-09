#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (48.83%)
# Likes:    3408
# Dislikes: 204
# Total Accepted:    320.3K
# Total Submissions: 654.2K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
#  '[[],[1],[2],[2],[],[1],[2],[]]'
#
# Implement the RandomizedSet class:
# 
# 
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns
# true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns
# true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is
# called). Each element must have the same probability of being returned.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# 
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was
# inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now
# contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2
# randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now
# contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set,
# getRandom() will always return 2.
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
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv_store = defaultdict(int)
        self.keys = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.kv_store:
            return False 
        else:
            self.keys.append(val)
            self.kv_store[val] = len(self.keys) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.kv_store:
            index = self.kv_store[val]
            del self.kv_store[val]

            if index == len(self.keys) - 1:
                self.keys.pop()
            else:
                item_moved = self.keys[-1]
                self.keys[index] = item_moved
                self.keys.pop()
                self.kv_store[item_moved] = index
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        length = len(self.keys)
        return self.keys[randrange(length)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

