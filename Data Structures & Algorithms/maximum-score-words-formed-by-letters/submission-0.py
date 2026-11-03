class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter

        available = Counter(letters)
        n = len(words)

        def backtrack(i):
            if i == n:
                return 0

            # Skip the current word
            ans = backtrack(i + 1)

            # Try selecting the current word
            word_count = Counter(words[i])
            word_score = 0

            for ch, count in word_count.items():
                if count > available[ch]:
                    return ans

                word_score += count * score[ord(ch) - ord('a')]

            # Use the letters
            for ch, count in word_count.items():
                available[ch] -= count

            ans = max(ans, word_score + backtrack(i + 1))

            # Restore the letters
            for ch, count in word_count.items():
                available[ch] += count

            return ans

        return backtrack(0)