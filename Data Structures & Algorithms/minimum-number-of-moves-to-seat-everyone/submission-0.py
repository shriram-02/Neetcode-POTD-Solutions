class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        moves = 0
        for s, t in zip(seats, students):
            moves += abs(s - t)
            
        return moves