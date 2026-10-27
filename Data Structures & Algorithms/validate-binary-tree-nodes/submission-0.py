
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [0] * n

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    parent[child] += 1
                    if parent[child] > 1:
                        return False

        roots = [i for i in range(n) if parent[i] == 0]

        if len(roots) != 1:
            return False

        root = roots[0]
        visited = set()
        stack = [root]

        while stack:
            node = stack.pop()

            if node in visited:
                return False

            visited.add(node)

            if leftChild[node] != -1:
                stack.append(leftChild[node])

            if rightChild[node] != -1:
                stack.append(rightChild[node])

        return len(visited) == n
