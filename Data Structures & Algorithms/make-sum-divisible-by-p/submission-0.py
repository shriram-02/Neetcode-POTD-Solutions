from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0
        last = {0: -1}
        prefix = 0
        ans = len(nums)

        for i , num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - target) % p

            if need in last:
                ans = min(ans, i - last[need])
            last[prefix] = i
        return -1 if ans == len(nums) else ans