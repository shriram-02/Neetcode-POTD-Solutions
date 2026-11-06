class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_count = {}

        for word in words:
            prefix = ""
            for ch in word:
                prefix += ch
                prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

        ans = []

        for word in words:
            score = 0
            prefix = ""
            for ch in word:
                prefix += ch
                score += prefix_count[prefix]
            ans.append(score)

        return ans