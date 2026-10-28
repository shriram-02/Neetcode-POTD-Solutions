class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque

        result = []
        queue = deque([root])

        while queue:
            level_max = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_max)

        return result