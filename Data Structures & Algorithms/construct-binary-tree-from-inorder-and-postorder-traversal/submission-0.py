# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left, right):
            nonlocal post_idx
            if left > right:
                return None

            val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(val)

            idx = index_map[val]
            root.right = build(idx + 1, right)
            root.left = build(left, idx - 1)

            return root

        return build(0, len(inorder) - 1)