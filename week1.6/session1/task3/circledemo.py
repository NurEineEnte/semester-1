# Week 1.6, Session 1: Task 3
from shapes import Circle
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
c1 = Circle(radius = 2.5)
print(c1)
print(c1.area(), c1.perimeter())
c1.set_position(3,1)
print(c1)
c1.set_colour("green")
print(c1.colour)