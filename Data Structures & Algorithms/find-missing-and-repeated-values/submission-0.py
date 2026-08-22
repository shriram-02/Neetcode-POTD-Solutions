from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n

        # Flatten the grid into a single list
        nums = [num for row in grid for num in row]

        # Frequency array
        freq = [0] * (total_numbers + 1)

        for num in nums:
            freq[num] += 1

        repeated = -1
        missing = -1

        for i in range(1, total_numbers + 1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i

        return [repeated, missing]
