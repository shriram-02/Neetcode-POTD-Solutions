class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        count = [0] * 26

        for word in words:
            for ch in word:
                count[ord(ch) - ord('a')] += 1

        return all(x % n == 0 for x in count)