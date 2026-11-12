import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Min-heap of available servers: (weight, index)
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        
        # Min-heap of busy servers: (free_time, weight, index)
        busy = []
        ans = []
        time = 0
        
        for j, duration in enumerate(tasks):
            # Advance clock to at least task arrival time
            time = max(time, j)
            
            # If no servers are free, jump forward to the earliest completion time
            if not free:
                time = max(time, busy[0][0])
            
            # Release all servers that have finished by the current time
            while busy and busy[0][0] <= time:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))
            
            # Assign the highest-priority free server
            w, idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (time + duration, w, idx))
            
        return ans