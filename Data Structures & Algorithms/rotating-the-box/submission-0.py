class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # Let stones fall to the right in each row
        for r in range(m):
            empty = n - 1

            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    empty = c - 1
                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty] = '#'
                    empty -= 1

        # Rotate 90 degrees clockwise
        res = [[None] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]

        return res