"""LeetCode 1: Two Sum."""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        1. iterate nums
        2. use dict {} to store all values visited (value, index)
        3. check if {target - num[i]} in dict
            3.1 if yes, return index (index, i)
            3.2 if not, put {value, i} in dict
        """
        dict_ = {}
        for i in range(len(nums)):
            value = nums[i]
            other_value = target - value
            if other_value in dict_:
                return [dict_[other_value], i]

            dict_[value] = i

if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3,4,5]
    target = 9
    result = s.twoSum(nums, target)
    assert result == [3, 4], f"actual result{result}"

    nums = [100,2,3,4,5]
    target = 102
    result = s.twoSum(nums, target)
    assert result == [0, 1], f"actual result{result}"

    nums = [100,100,3,4,5]
    target = 200
    result = s.twoSum(nums, target)
    assert result == [0, 1], f"actual result{result}"
