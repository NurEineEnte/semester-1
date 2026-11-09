# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import math
import unittest

class Test_geometry(unittest.TestCase):

    def test_point_constructor(self):
        p = Point(5, -2)
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, -2)

    def test_point_distance(self):
        self.assertEqual(Point(0, 0).distance(), 0.0)
        self.assertEqual(Point(6, 8).distance(), 10.0)

        
    def test_point_distance_to(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(p1.distance_to(p2), 5)
        # complete the implementation for
        # testing distance_to()
        

    # Write test functions to test the __init__(), 
    # area() and perimeter() methods in Circle class
    # you can use the default value for centre coordinates

    def test_circle_constructor(self):
        c = Circle(5)
        self.assertEqual([c.centre.x, c.centre.y], [0,0])
        self.assertEqual(c.radius, 5)

    def test_circle_area(self):
        c = Circle(8)
        self.assertEqual(c.area(), math.pi*8**2)
        c1 = Circle(5)
        self.assertEqual(c1.area(), math.pi * 5 **2)


    def test_circle_perimeter(self):
        c = Circle(8)
        self.assertEqual(c.perimeter(), 8*2*math.pi)

if __name__ == '__main__':
    unittest.main()