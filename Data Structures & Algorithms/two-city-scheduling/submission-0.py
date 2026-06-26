class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])

        n = len(costs) // 2
        ans = 0

        for i in range(n):
            ans += costs[i][1]      # Send to B

        for i in range(n, 2 * n):
            ans += costs[i][0]      # Send to A

        return ans