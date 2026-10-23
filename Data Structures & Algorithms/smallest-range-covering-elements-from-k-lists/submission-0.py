from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float('-inf')

        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            max_val = max(max_val, arr[0])

        best_left = heap[0][0]
        best_right = max_val

        while True:
            min_val, i, j = heapq.heappop(heap)

            if max_val - min_val < best_right - best_left or (
                max_val - min_val == best_right - best_left
                and min_val < best_left
            ):
                best_left, best_right = min_val, max_val

            if j + 1 == len(nums[i]):
                break

            next_val = nums[i][j + 1]
            heapq.heappush(heap, (next_val, i, j + 1))
            max_val = max(max_val, next_val)

        return [best_left, best_right]