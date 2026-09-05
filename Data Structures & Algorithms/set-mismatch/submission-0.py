class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        
        duplicate = 0
        for x in nums:
            if x in seen:
                duplicate = x
            seen.add(x)
        
        missing = next(x for x in range(1, n + 1) if x not in seen)
        
        return [duplicate, missing]