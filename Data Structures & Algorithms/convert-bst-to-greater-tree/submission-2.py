class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()

            total += curr.val
            curr.val = total

            curr = curr.left

        return root