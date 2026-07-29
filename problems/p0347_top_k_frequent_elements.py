"""LeetCode 347: Top K Frequent Elements."""

from collections import Counter
import heapq
import logging

logger = logging.getLogger(__name__)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Return the k most frequent elements from nums, in any order."""
        counts = Counter(nums)
        logger.debug("count stats of nums: %s", counts)

        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (-freq, num))

        logger.debug("priority queue: %s", heap)
        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)

        return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    s = Solution()

    # base case
    nums = [1,2,2,3,3,3] 
    k = 2

    expect = [2,3]
    result = s.topKFrequent(nums, k) 
    assert sorted(result) == expect, f"expect {expect}, but {result}"

    # k == len(nums)
    nums = [1,2,2,3,3,3] 
    k = 3  

    expect = [1,2,3]
    result = s.topKFrequent(nums, k) 
    assert sorted(result) == expect, f"expect {expect}, but {result}"

    # k == 1
    nums = [1,2,2,3,3,3] 
    k = 1  

    expect = [3]
    result = s.topKFrequent(nums, k) 
    assert sorted(result) == expect, f"expect {expect}, but {result}"

    # k == 2, with negative number
    nums = [1,2,2,-3,-3,-3] 
    k = 2  

    expect = [-3, 2]
    result = s.topKFrequent(nums, k) 
    assert sorted(result) == expect, f"expect {expect}, but {result}"

    # k == 3, with zeros
    nums = [1,2,2,-3,-3,-3, 0, 0, 0, 0] 
    k = 3  

    expect = [-3, 0, 2]
    result = s.topKFrequent(nums, k) 
    assert sorted(result) == expect, f"expect {expect}, but {result}"
