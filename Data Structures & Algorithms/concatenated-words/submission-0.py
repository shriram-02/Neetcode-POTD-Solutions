class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        res = []

        def canForm(word):
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue

                    if j == 0 and i == n:
                        continue

                    if word[j:i] in wordSet:
                        dp[i] = True
                        break

            return dp[n]

        for word in words:
            if canForm(word):
                res.append(word)

        return res