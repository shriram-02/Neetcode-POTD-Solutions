class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[pos] = nums[left] * nums[left]
                left += 1
            else:
                ans[pos] = nums[right] * nums[right]
                right -= 1

            pos -= 1

        return ans