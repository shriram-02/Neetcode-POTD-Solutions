from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        steps = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return steps
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx, ny))
            steps += 1