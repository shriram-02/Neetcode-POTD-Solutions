class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        ans = 0

        for x in nums:
            ans += count.get(x, 0)
            count[x] = count.get(x, 0) + 1

        return ans