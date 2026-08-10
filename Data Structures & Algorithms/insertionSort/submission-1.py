class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        res = [pairs.copy()]

        for i in range(1, len(pairs)):
            j = i

            while j > 0 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1

            res.append(pairs.copy())

        return res