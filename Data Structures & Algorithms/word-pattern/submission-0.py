class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Number of pattern characters and words must match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):

            # ch already has a mapping
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False

            # word already belongs to another character
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False

            # Establish the mapping
            char_to_word[ch] = word
            word_to_char[word] = ch

        return True