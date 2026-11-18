from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if not q or len(q) == n * n:
            return -1

        dist = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))

            dist += 1

        return dist