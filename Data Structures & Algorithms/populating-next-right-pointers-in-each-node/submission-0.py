class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root