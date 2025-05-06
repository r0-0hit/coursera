import math


def calculate_area_circle(radius: float) -> float:
    """Calculates the area of a circle given its radius."""
    area = math.pi * radius**2
    return area


def calculate_circumference_circle(radius: float) -> float:
    """Calculates the circumference of a circle given its radius."""
    return 2 * math.pi * radius


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def calculate_perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
