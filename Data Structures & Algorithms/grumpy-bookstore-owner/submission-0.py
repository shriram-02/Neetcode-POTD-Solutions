class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int):
        n = len(customers)

        # Customers already satisfied
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # Extra customers that can be satisfied in first window
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        # Sliding window
        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra