
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_wait = 0

        for arrival, time in customers:
            # Chef waits until the customer arrives if he is idle
            current_time = max(current_time, arrival)

            # Finish preparing this order
            current_time += time

            # Customer waits from arrival until order is finished
            total_wait += current_time - arrival

        return total_wait / len(customers)

