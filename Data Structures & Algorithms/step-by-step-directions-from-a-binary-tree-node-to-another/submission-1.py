class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(target):
            stack = [(root, "")]

            while stack:
                node, path = stack.pop()

                if node.val == target:
                    return path

                if node.right:
                    stack.append((node.right, path + "R"))

                if node.left:
                    stack.append((node.left, path + "L"))

        startPath = findPath(startValue)
        destPath = findPath(destValue)

        i = 0
        while i < min(len(startPath), len(destPath)) and startPath[i] == destPath[i]:
            i += 1

        return "U" * (len(startPath) - i) + destPath[i:]