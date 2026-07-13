from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = max(v for v in freq.values() if v % 2)
        even = min(v for v in freq.values() if v % 2 == 0)
        return odd - even