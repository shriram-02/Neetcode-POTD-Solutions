class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(s):
            if len(s) == n:
                ans.append(s)
                return

            for ch in "abc":
                if not s or s[-1] != ch:
                    backtrack(s + ch)

        backtrack("")

        return ans[k - 1] if k <= len(ans) else ""