class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch in first:
                ans = max(ans, i - first[ch] - 1)
            else:
                first[ch] = i

        return ans