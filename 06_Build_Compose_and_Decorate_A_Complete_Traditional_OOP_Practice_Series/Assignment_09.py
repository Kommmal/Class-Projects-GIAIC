from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Rectangle():

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height
    
rect1 = Rectangle(5, 3)

print("Area of rectangle:", rect1.area())