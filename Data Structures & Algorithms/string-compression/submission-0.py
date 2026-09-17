class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1
            count = j - i
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            i = j
        return write
