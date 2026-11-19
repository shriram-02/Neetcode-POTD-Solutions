class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root):
            if not root:
                return []

            if not root.left and not root.right:
                return [root.val]

            return getLeaves(root.left) + getLeaves(root.right)

        return getLeaves(root1) == getLeaves(root2)