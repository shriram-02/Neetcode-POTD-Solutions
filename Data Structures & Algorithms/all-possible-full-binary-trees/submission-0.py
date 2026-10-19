class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        memo = {1: [TreeNode(0)]}

        def build(n):
            if n in memo:
                return memo[n]

            trees = []
            for left_size in range(1, n, 2):
                right_size = n - 1 - left_size

                for left in build(left_size):
                    for right in build(right_size):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        trees.append(root)

            memo[n] = trees
            return trees

        return build(n) if n % 2 == 1 else []