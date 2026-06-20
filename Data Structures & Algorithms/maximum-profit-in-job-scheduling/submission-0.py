from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        
        ends = [e for e, _, _ in jobs]
        dp = [0] * (len(jobs) + 1)

        for i, (e, s, p) in enumerate(jobs, 1):
            j = bisect_right(ends, s)
            dp[i] = max(dp[i - 1], dp[j] + p)

        return dp[-1]