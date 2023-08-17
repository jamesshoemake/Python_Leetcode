from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # weights are negative, so reversed logic
            if second > first:
                heapq.heappush(stones, first - second)
        # and 0 to stones.incase the heap is empty.
        stones.append(0)
        return abs(stones[0])
