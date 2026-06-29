class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        pairs = []

        for i in range(len(weights) - 1):
            pairs.append(weights[i] + weights[i + 1])

        pairs.sort()

        ans = 0
        for i in range(k - 1):
            ans += pairs[-(i + 1)] - pairs[i]

        return ans