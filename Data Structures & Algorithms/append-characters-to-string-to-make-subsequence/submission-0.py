class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0  # pointer for t

        for ch in s:
            if j < len(t) and ch == t[j]:
                j += 1

        # remaining characters in t need to be appended
        return len(t) - j