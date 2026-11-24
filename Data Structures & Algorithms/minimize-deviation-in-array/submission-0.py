import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_val = float('inf')

        for num in nums:
            if num % 2 == 1:
                num *= 2

            heapq.heappush(max_heap, -num)
            min_val = min(min_val, num)

        ans = float('inf')

        while True:
            max_val = -heapq.heappop(max_heap)

            ans = min(ans, max_val - min_val)

            if max_val % 2 == 1:
                break

            max_val //= 2
            min_val = min(min_val, max_val)

            heapq.heappush(max_heap, -max_val)

        return ans