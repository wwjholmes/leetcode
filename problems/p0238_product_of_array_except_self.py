"""LeetCode 238: Product of Array Except Self."""

import logging

class Solution:
    logger = logging.getLogger(__name__)

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Return an array where output[i] is the product of all elements of
        nums except nums[i].

        Each product is guaranteed to fit in a 32-bit integer.
        Constraints: 2 <= len(nums) <= 1000, -20 <= nums[i] <= 20.
        """
        # calculate the product [:i] left_proudct
        left = []
        product = 1
        for i in range(len(nums)):
            left.append(product)
            product *= nums[i]
        self.logger.debug(f"left: {left}")

        # calcualte the product [i:] right_product
        right = []
        product = 1
        for i in range(len(nums)):
            right.append(product)
            product *= nums[len(nums) - 1 - i]

        right.reverse()
        self.logger.debug(f"right: {right}")

        # then iterate again, result[i] = left_product[i] * right_product[i]
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        self.logger.debug(f"result: {result}")
        return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=f"%(message)s")
    s = Solution()

    # test case 1
    nums = [1, 2, 3, 4]
    actual = s.productExceptSelf(nums)
    assert actual == [24, 12, 8, 6], f"actual is {actual}"

    # test case 2
    nums = [0, 2, 3, 4]
    actual = s.productExceptSelf(nums)
    assert actual == [24, 0, 0, 0], f"actual is {actual}"
