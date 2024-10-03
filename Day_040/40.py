import math

# Base class for all shapes
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass  # Will be implemented in derived classes
    
    def perimeter(self):
        pass  # Will be implemented in derived classes

    def describe(self):
        print(f"This is a {self.name}.")

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Derived class for Square
class Square(Shape):
    def __init__(self, side_length):
        super().__init__("Square")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 3, 4, 5)

circle.describe()
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")

square.describe()
print(f"Square area: {square.area()}")
print(f"Square perimeter: {square.perimeter()}")

triangle.describe()
print(f"Triangle area: {triangle.area()}")
print(f"Triangle perimeter: {triangle.perimeter()}")
