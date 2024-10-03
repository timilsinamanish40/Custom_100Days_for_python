import math

# Base class
class Shape:
    def area(self):
        pass

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Create objects of Circle and Triangle
shapes = [
    Circle(5),         # Circle with radius 5
    Triangle(3, 7)     # Triangle with base 3 and height 7
]

# Polymorphism in action
for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")
