class Square:
    def __init__(self, sideLength=0.0):
        self.sideLength = sideLength

    def getSideLength(self) -> float:
        return self.sideLength
    
class SquareHole:
    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def canFit(self, square: Square):
        return self.sideLength >= square.getSideLength()

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getRadius(self):
        return self.radius

class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
        self.circle = circle
    
    def getSideLength(self) -> float:
        return 2 * self.circle.getRadius()