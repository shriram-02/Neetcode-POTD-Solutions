
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = [0] * 26

        # Count characters available in chars
        for ch in chars:
            char_count[ord(ch) - ord('a')] += 1

        ans = 0

        for word in words:
            word_count = [0] * 26
            possible = True

            for ch in word:
                idx = ord(ch) - ord('a')
                word_count[idx] += 1

                if word_count[idx] > char_count[idx]:
                    possible = False
                    break

            if possible:
                ans += len(word)

        return ans

