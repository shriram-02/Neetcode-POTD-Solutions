import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            x = -heapq.heappop(heap)
            heapq.heappush(heap, -math.isqrt(x))

        return -sum(heap)