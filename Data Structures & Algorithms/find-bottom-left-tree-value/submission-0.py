class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]

        while queue:
            node = queue.pop(0)
            ans = node.val

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return ans