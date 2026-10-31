class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        q = deque([root])
        level = 0

        while q:
            prev = float('-inf') if level % 2 == 0 else float('inf')

            for _ in range(len(q)):
                node = q.popleft()
                val = node.val

                if level % 2 == 0:
                    if val % 2 == 0 or val <= prev:
                        return False
                else:
                    if val % 2 != 0 or val >= prev:
                        return False

                prev = val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return True