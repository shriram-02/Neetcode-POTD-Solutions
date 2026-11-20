class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq

        heap = []

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb > 0:
                heapq.heappush(heap, climb)

            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)

            if bricks < 0:
                return i

        return len(heights) - 1