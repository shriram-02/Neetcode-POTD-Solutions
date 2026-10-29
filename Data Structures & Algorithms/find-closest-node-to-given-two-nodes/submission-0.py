class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def getDistances(start):
            dist = [-1] * n
            d = 0
            node = start

            while node != -1 and dist[node] == -1:
                dist[node] = d
                d += 1
                node = edges[node]

            return dist

        dist1 = getDistances(node1)
        dist2 = getDistances(node2)

        ans = -1
        minDist = float('inf')

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                maxDist = max(dist1[i], dist2[i])

                if maxDist < minDist:
                    minDist = maxDist
                    ans = i

        return ans