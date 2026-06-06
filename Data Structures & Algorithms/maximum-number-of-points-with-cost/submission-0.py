class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        dp = points[0][:]

        for i in range(1, m):
            left = [0] * n
            right = [0] * n

            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, dp[j])

            right[n - 1] = dp[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, dp[j])

            new_dp = [0] * n
            for j in range(n):
                new_dp[j] = points[i][j] + max(left[j], right[j])

            dp = new_dp

        return max(dp)