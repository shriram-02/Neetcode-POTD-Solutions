import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []

        for left, right in intervals:
            if heap and heap[0] < left:
                heapq.heappop(heap)
            heapq.heappush(heap, right)

        return len(heap)