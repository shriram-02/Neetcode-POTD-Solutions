class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            cost1 = costs[0] + dp[j]

            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            cost7 = costs[1] + dp[j]

            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            cost30 = costs[2] + dp[j]

            dp[i] = min(cost1, cost7, cost30)

        return dp[0]