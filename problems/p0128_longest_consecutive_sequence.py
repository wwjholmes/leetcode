"""LeetCode 128: Longest Consecutive Sequence."""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Return the length of the longest consecutive sequence of elements
        that can be formed from `nums`.

        A consecutive sequence has each element exactly 1 greater than the
        previous element; elements need not be consecutive in the original
        array. Must run in O(n) time.
        """
        nums_set = set(nums)
        max_seq = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            seq = n
            while seq in nums_set:
                seq += 1
            max_seq = max(max_seq, seq - n)
        return max_seq


if __name__ == "__main__":
    s = Solution()

    # test case 1
    nums = [2, 20, 4, 10, 3, 4, 5]
    result = s.longestConsecutive(nums)
    assert result == 4, f"actual is {result}"

    # test case 2
    nums = [0,3,2,5,4,6,1,1]
    result = s.longestConsecutive(nums)
    assert result == 7, f"actual is {result}"

    # boundary: empty input
    assert s.longestConsecutive([]) == 0

    # boundary: all duplicates collapse to one sequence of length 1
    assert s.longestConsecutive([1, 1, 1]) == 1

    # boundary: sequence spanning negative and positive values
    assert s.longestConsecutive([-3, -2, -1, 0]) == 4

