class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        
        if old == color:
            return image
        
        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != old:
                return
            
            image[r][c] = color
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image