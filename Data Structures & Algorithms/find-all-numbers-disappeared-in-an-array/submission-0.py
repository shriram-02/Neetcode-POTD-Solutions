class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            i = abs(x) - 1
            nums[i] = -abs(nums[i])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]