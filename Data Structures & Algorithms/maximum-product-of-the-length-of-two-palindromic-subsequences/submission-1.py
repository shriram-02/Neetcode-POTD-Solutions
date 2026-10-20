class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        total = 1 << n
        pal = [0] * total

        for mask in range(1, total):
            subseq = []
            for i in range(n):
                if mask & (1 << i):
                    subseq.append(s[i])

            if subseq == subseq[::-1]:
                pal[mask] = len(subseq)

        ans = 0
        full = total - 1

        for mask in range(1, total):
            if pal[mask] == 0:
                continue

            remaining = full ^ mask
            sub = remaining

            while sub:
                if pal[sub]:
                    ans = max(ans, pal[mask] * pal[sub])
                sub = (sub - 1) & remaining

        return ans