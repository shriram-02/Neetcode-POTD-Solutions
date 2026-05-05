class Solution {
public:
    int diameter = 0;

    int depth(TreeNode* root) {
        if (!root) return 0;

        int left = depth(root->left);
        int right = depth(root->right);

        diameter = max(diameter, left + right);

        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return diameter;
    }
};