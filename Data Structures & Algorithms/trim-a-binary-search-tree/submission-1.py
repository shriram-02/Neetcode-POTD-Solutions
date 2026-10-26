
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left

        if not root:
            return None

        node = root
        while node:
            while node.left and node.left.val < low:
                node.left = node.left.right
            node = node.left

        node = root
        while node:
            while node.right and node.right.val > high:
                node.right = node.right.left
            node = node.right

        return root
