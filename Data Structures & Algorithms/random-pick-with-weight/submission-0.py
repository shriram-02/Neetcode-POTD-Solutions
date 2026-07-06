import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        s = 0
        for x in w:
            s += x
            self.prefix.append(s)
        self.total = s

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()