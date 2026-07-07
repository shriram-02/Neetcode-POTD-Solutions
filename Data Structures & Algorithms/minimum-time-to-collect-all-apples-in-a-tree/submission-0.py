from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            time = 0
            for nei in graph[node]:
                if nei != parent:
                    t = dfs(nei, node)
                    if t > 0 or hasApple[nei]:
                        time += t + 2
            return time

        return dfs(0, -1)