from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        # Traverse from right to left
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)

        return arr