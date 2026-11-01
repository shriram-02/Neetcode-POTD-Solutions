class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        delete_set = set(to_delete)
        forest = []
        stack = [(root, None, False)]

        while stack:
            node, parent, is_left = stack.pop()

            if not node:
                continue

            deleted = node.val in delete_set

            if parent:
                if is_left:
                    parent.left = None if deleted else node
                else:
                    parent.right = None if deleted else node

            if not deleted and (parent is None or parent.val in delete_set):
                forest.append(node)

            stack.append((node.right, node, False))
            stack.append((node.left, node, True))

        return forest