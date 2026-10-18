from typing import List

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [-1] * len(parent)
        self.children = [[] for _ in parent]

        for i in range(1, len(parent)):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False

        self.locked[num] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False

        curr = self.parent[num]
        while curr != -1:
            if self.locked[curr] != -1:
                return False
            curr = self.parent[curr]

        descendants = []
        stack = self.children[num][:]

        while stack:
            node = stack.pop()
            if self.locked[node] != -1:
                descendants.append(node)
            stack.extend(self.children[node])

        if not descendants:
            return False

        for node in descendants:
            self.locked[node] = -1

        self.locked[num] = user
        return True