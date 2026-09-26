class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for ch in order:
            idx = ord(ch) - ord('a')
            ans.append(ch * count[idx])
            count[idx] = 0

        for i in range(26):
            if count[i]:
                ans.append(chr(i + ord('a')) * count[i])

        return ''.join(ans)