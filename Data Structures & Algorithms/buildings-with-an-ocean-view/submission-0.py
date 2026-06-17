class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        mx = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > mx:
                res.append(i)
                mx = heights[i]

        return res[::-1]