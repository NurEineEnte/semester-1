# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle
p1 = Point(1,2)
c1 = Circle(5, p1)
p2 = Point(3,3)
if p2 in c1:
    print(f"point in circle")
else:
    print(f"point not in circle")