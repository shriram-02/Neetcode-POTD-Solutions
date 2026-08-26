class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = [0] * 501

        for x in nums:
            freq[x] += 1

        for count in freq:
            if count % 2 != 0:
                return False

        return True