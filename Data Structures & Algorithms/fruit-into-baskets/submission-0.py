class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        ans = 0

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans