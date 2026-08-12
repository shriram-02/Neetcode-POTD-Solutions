class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}

        for s in arr:
            freq[s] = freq.get(s, 0) + 1

        for s in arr:
            if freq[s] == 1:
                k -= 1
                if k == 0:
                    return s

        return ""