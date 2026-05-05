class Solution {
public:
    int dfs(TreeNode* node, int maxSoFar) {
        if (!node) return 0;

        int count = 0;
        if (node->val >= maxSoFar) {
            count = 1;
            maxSoFar = node->val;
        }

        count += dfs(node->left, maxSoFar);
        count += dfs(node->right, maxSoFar);

        return count;
    }

    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
};