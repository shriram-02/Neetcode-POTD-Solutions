class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        
        for ch in s:
            x ^= ord(ch)
        
        for ch in t:
            x ^= ord(ch)
        
        return chr(x)