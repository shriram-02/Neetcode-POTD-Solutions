class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sums = []

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                sums.append(total)

        sums.sort()

        return sum(sums[left - 1:right]) % MOD