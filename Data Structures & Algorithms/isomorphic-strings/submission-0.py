class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        for a, b in zip(s, t):
            if a in mp1:
                if mp1[a] != b:
                    return False
            else:
                mp1[a] = b

            if b in mp2:
                if mp2[b] != a:
                    return False
            else:
                mp2[b] = a

        return True