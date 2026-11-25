class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num

        count = 0

        def backtrack(index, curr_or):
            nonlocal count

            if index == len(nums):
                if curr_or == max_or:
                    count += 1
                return

            # Include current element
            backtrack(index + 1, curr_or | nums[index])

            # Exclude current element
            backtrack(index + 1, curr_or)

        backtrack(0, 0)

        return count