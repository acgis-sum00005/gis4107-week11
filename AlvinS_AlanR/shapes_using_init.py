import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def circle_radius(self):
        return self.radius
        
    @property
    def circle_area(self):
        self.__area = round(math.pi * (self.radius ** 2), 3)
        return self.__area

    def __str__(self):
        return f'Circle area with a radius of {self.circle_radius} is {self.circle_area}'


class Square:
    def __init__(self, side):
        self.side = side
    
    @property
    def square_side(self):
        return self.side
    
    @property
    def square_area(self):
        self.__area = self.side ** 2
        return self.__area

    def __str__(self):
        return f'Square area with a side of {self.square_side} is {self.square_area}'

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def rectangle_width(self):
        return self.width

    @property
    def rectangle_height(self):
        return self.height

    @property
    def rectangle_area(self):
        self.__area = self.width * self.height
        return self.__area

    def __str__(self):
        return f'Rectangle area with a width of {self.rectangle_width} and height of {self.rectangle_height} is {self.rectangle_area}'
        

    
    