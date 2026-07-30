class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            left = 0
            s = 0
            ans = 0
            for right in range(len(nums)):
                s += nums[right]
                while s > k:
                    s -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans

        return atMost(goal) - atMost(goal - 1)