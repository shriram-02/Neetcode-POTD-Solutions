class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count white blocks in the first window
        white = blocks[:k].count('W')
        ans = white

        # Slide the window
        for i in range(k, len(blocks)):
            # Remove left character
            if blocks[i - k] == 'W':
                white -= 1

            # Add right character
            if blocks[i] == 'W':
                white += 1

            ans = min(ans, white)

        return ans