# Another bad class implementation

# What does the runtime error mean?
#class does not have an attribute that it is trying to access, as it was defined as a local variable rather than an attribute
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
