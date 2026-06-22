class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        pos, neg = 0, 1

        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2

        return ans