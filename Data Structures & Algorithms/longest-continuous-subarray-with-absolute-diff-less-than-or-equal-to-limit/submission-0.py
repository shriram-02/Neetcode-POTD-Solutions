class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque

        max_dq = deque()
        min_dq = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()
            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()

            max_dq.append(right)
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans