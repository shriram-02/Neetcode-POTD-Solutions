/**
 * // Definition for a QuadTree node.
 * class Node {
 *     constructor(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *         this.val = val;
 *         this.isLeaf = isLeaf;
 *         this.topLeft = topLeft;
 *         this.topRight = topRight;
 *         this.bottomLeft = bottomLeft;
 *         this.bottomRight = bottomRight;
 *     }
 * }
 */

class Solution {
    /**
     * @param {number[][]} grid
     * @return {Node}
     */
    construct(grid) {
        const build = (row, col, size) => {
            let same = true;
            let value = grid[row][col];

            for (let i = row; i < row + size; i++) {
                for (let j = col; j < col + size; j++) {
                    if (grid[i][j] !== value) {
                        same = false;
                        break;
                    }
                }

                if (!same) break;
            }

            if (same) {
                return new Node(value === 1, true, null, null, null, null);
            }

            let half = size / 2;

            return new Node(
                true,
                false,
                build(row, col, half),
                build(row, col + half, half),
                build(row + half, col, half),
                build(row + half, col + half, half)
            );
        };

        return build(0, 0, grid.length);
    }
}