from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = sorted(Counter(arr).values())

        unique = len(freq)

        for count in freq:
            if k >= count:
                k -= count
                unique -= 1
            else:
                break

        return unique