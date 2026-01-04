#!/usr/bin/env python3
"""Task 1: Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class representing geometric shapes
    
    Requires implementing classes to define area and perimeter calculations
    """
    
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the shape's area
        
        Returns:
            float: The calculated area
        """
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the shape's perimeter
        
        Returns:
            float: The calculated perimeter
        """
        pass

class Circle(Shape):
    """Circle shape defined by its radius"""
    
    def __init__(self, radius: float):
        """Initialize with radius value
        
        Args:
            radius: The circle's radius (absolute value used for calculations)
        """
        self.radius = radius
    
    def area(self) -> float:
        """Calculate area using πr² formula"""
        return math.pi * abs(self.radius) ** 2
    
    def perimeter(self) -> float:
        """Calculate circumference using 2πr formula"""
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    """Rectangle shape defined by width and height"""
    
    def __init__(self, width: float, height: float):
        """Initialize with width and height values
        
        Args:
            width: The rectangle's width
            height: The rectangle's height
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate area using width × height formula"""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate perimeter using 2(width + height) formula"""
        return 2 * (self.width + self.height)

def shape_info(shape: Shape):
    """Print shape's area and perimeter using duck typing
    
    Args:
        shape: Any object implementing area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Demonstration when run directly
    circle = Circle(5)
    rectangle = Rectangle(4, 7)
    
    shape_info(circle)
    shape_info(rectangle)
