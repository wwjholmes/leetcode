"""LeetCode 15: 3Sum."""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Return all unique triplets [a, b, c] from distinct indices with a + b + c == 0.

        The result must not contain duplicate triplets; output and triplet
        order do not matter. Constraints: 3 <= len(nums) <= 1000,
        -10**5 <= nums[i] <= 10**5.
        """
        sorted_nums = sorted(nums)

        results = set()
        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    results.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
        return [list(triplet) for triplet in results]


if __name__ == "__main__":
    s = Solution()

    # representative case: two triplets
    nums = [-1, 0, 1, 2, -1, -4]
    result = s.threeSum(nums)
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]]), f"got {result}"

    # no triplet sums to zero
    nums = [0, 1, 1]
    result = s.threeSum(nums)
    assert result == [], f"got {result}"

    # all zeros
    nums = [0, 0, 0]
    result = s.threeSum(nums)
    assert result == [[0, 0, 0]], f"got {result}"

    # duplicates must collapse into one triplet
    nums = [-2, 0, 0, 2, 2]
    result = s.threeSum(nums)
    assert result == [[-2, 0, 2]], f"got {result}"

    print("All tests passed.")