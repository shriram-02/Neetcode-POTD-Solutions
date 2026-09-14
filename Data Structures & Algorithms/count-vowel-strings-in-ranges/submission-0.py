
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i] + (
                word[0] in vowels and word[-1] in vowels
            )

        return [prefix[r + 1] - prefix[l] for l, r in queries]

