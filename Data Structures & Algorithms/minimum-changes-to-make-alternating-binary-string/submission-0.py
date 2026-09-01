class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        changes0 = 0
        changes1 = 0

        for i, ch in enumerate(s):
            if ch != ('0' if i % 2 == 0 else '1'):
                changes0 += 1
            if ch != ('1' if i % 2 == 0 else '0'):
                changes1 += 1

        return min(changes0, changes1)