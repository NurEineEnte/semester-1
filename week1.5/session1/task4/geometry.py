# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
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
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    def area(self):
        area = math.pi * self.radius * self.radius
        return area
    def perimeter(self):
        perimeter = math.pi * 2 * self.radius
        return perimeter



# Don't add any testing code to this file!
