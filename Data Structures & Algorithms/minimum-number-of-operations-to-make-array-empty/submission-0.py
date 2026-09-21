class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        ans = 0

        for count in freq.values():
            if count == 1:
                return -1
            ans += count // 3
            count %= 3
            if count:
                ans += 1
        return ans