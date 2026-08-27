from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        # Largest two numbers
        max1, max2 = nums[-1], nums[-2]
        # Smallest two numbers
        min1, min2 = nums[0], nums[1]
        # Compute product difference
        return (max1 * max2) - (min1 * min2)
