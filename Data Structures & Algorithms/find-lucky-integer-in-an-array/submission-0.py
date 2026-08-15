class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * 501

        for x in arr:
            freq[x] += 1

        for x in range(500, 0, -1):
            if freq[x] == x:
                return x

        return -1