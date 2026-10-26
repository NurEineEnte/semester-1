# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """
    # Add constructor here
    def __init__(self, xvalue, yvalue):
        self.x = xvalue
        self.y = yvalue
    
    def distance(self):
        distance = math.sqrt(self.x ** 2 + self.y ** 2)
        return distance
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distanceto(self, x2, y2):
        xdif = x2 - self.x
        ydif = y2 - self.y
        distance = math.sqrt(xdif** 2 + ydif ** 2)
        return distance


# Finally, add code here to demonstrate use of Point
mypoint = Point(5,2)
print(f"distance to origin is: {mypoint.distance()}")
print(f"distance between ({mypoint.x}, {mypoint.y}) and (9, -5) is {mypoint.distanceto(9,-5)}")