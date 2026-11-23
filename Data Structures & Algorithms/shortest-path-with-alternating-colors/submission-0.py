from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[] for _ in range(2)] for _ in range(n)]

        for u, v in redEdges:
            graph[u][0].append(v)

        for u, v in blueEdges:
            graph[u][1].append(v)

        dist = [[-1] * 2 for _ in range(n)]
        dist[0] = [0, 0]

        q = deque([(0, 0), (0, 1)])

        while q:
            node, color = q.popleft()

            next_color = 1 - color

            for nei in graph[node][next_color]:
                if dist[nei][next_color] == -1:
                    dist[nei][next_color] = dist[node][color] + 1
                    q.append((nei, next_color))

        ans = []

        for r, b in dist:
            if r == -1:
                ans.append(b)
            elif b == -1:
                ans.append(r)
            else:
                ans.append(min(r, b))

        return ans