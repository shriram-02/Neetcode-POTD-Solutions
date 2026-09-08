class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev

            if not node:
                return

            inorder(node.left)

            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node

            prev = node
            inorder(node.right)

        inorder(root)

        first.val, second.val = second.val, first.val