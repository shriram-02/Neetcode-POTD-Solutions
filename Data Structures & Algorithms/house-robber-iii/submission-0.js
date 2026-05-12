/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    rob(root) {
        const dfs = (node) => {
            if (!node) return [0, 0];

            const left = dfs(node.left);
            const right = dfs(node.right);

            const robCurrent =
                node.val + left[1] + right[1];

            const skipCurrent =
                Math.max(left[0], left[1]) +
                Math.max(right[0], right[1]);

            return [robCurrent, skipCurrent];
        };

        const result = dfs(root);

        return Math.max(result[0], result[1]);
    }
}