
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                segment = s[index:index + length]

                if len(segment) > 1 and segment[0] == '0':
                    break

                if int(segment) > 255:
                    break

                backtrack(index + length, parts + [segment])

        backtrack(0, [])
        return result
