class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0

        for i in range(26):
            ch = chr(ord('a') + i)

            left = s.find(ch)
            right = s.rfind(ch)

            if left < right:
                seen = [False] * 26

                for j in range(left + 1, right):
                    seen[ord(s[j]) - ord('a')] = True

                ans += sum(seen)

        return ans