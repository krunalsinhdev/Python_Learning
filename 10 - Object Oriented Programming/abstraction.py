# Abstraction
# An abstract class defines methods that child classes must implement.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print("Rectangle area:", rectangle.area())
