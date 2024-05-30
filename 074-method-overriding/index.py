class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(3, 5)
print(rectangle.area())


class Circle(Rectangle):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22 / 7 * self.radius**2


circle = Circle(7)
print(circle.area())
