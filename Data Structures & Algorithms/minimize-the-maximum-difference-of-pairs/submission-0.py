class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can(diff):
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    pairs += 1
                    i += 2
                else:
                    i += 1
            return pairs >= p

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1

        return left