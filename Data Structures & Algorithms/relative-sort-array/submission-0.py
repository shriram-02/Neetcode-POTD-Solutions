from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []

        for x in arr2:
            ans.extend([x] * cnt[x])
            del cnt[x]

        for x in sorted(cnt.keys()):
            ans.extend([x] * cnt[x])

        return ans