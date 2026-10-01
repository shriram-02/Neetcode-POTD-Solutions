class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            j = i
            line_len = 0

            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            word_count = j - i
            spaces = maxWidth - line_len

            if j == len(words) or word_count == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                gaps = word_count - 1
                extra = spaces // gaps
                remainder = spaces % gaps

                line = ""

                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (extra + (1 if k < remainder else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result