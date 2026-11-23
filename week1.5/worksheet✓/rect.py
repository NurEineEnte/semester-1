# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError
        if width <= 0 or height <= 0:
            raise ValueError
        self.width = width
        self.height = height
    def is_square(self):
        """returns square if width and height are same"""
        if self.width == self.height:
            return True
        else:
            return False
    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
