from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        left = 0
        max_kept = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] >= n:
                left += 1
            max_kept = max(max_kept, right - left + 1)

        return n - max_kept