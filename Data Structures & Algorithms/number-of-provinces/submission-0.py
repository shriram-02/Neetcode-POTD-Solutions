class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n

        def dfs(u):
            vis[u] = True
            for v in range(n):
                if isConnected[u][v] and not vis[v]:
                    dfs(v)

        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)

        return ans