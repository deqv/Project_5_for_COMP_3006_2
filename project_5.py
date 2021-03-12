class Shape:
    def __init__(self, length_1, length_2):
        self.first = length_1
        self.second = length_2

    def area(length_1, length_2):
        pass

# The following is a class for Ovals, which contains the two radiuses that define the Oval
class Oval(Shape):
    def __init__(self, first_radius, second_radius):
        self.first = first_radius
        self.second = second_radius

    self.area = 3.1415 * first_radius*second_radius

# The following is a class for Rectangles, which contains the length and the width that define the Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    self.area = length*width

# The following is a class for Squares, which contains the length of any of the sides. The length defines the Square
class Square(Shape):
    def __init__(self, length):
        self.length=length

    self.area = length*length

# The following is a class for Triangle, which contains the base and the height. These two values allows us to calculate the area.
class Triangle(Shape):
    def __init__(self, base, height)
        self.base = base
        self.height = height

    self.area = .5 * base * height


class Pentagon(Shape):
    # Assuming identical lengths below
    def __init__(self, length):
        self.length=length

# The following is a class for Circle, which contains the radius. The radius not only defines the Circle but it also allows us to calculate the area.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    self.area = 3.1415 * radius * radius

# The following is a class for Parallelogram, which contains the base and the height. These two values allows us to calculate the area.
class Parallelogram(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    self.area = base * height
