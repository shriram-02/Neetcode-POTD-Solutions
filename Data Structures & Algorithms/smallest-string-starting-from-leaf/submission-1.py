class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = "{"
        stack = [(root, "")]

        while stack:
            node, path = stack.pop()

            path = chr(node.val + ord('a')) + path

            if not node.left and not node.right:
                ans = min(ans, path)
                continue

            if node.left:
                stack.append((node.left, path))

            if node.right:
                stack.append((node.right, path))

        return ans