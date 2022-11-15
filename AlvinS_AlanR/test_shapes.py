import shapes as shapes
import pytest
import math

def test_area_of_circle():
    
    expected = round(4 * math.pi, 3)
    circle = shapes.Circle()
    circle.radius = 2
    actual = circle.circle_area 
    assert expected == actual

    expected = "Circle area with a radius of 2 is 12.566"
    actual = str(circle)
    assert expected == actual


def test_area_of_square():

    expected = 9
    square = shapes.Square()
    square.side = 3
    actual = square.square_area
    assert expected == actual

    expected = "Square area with a side of 3 is 9"
    actual = str(square)
    assert expected == actual

def test_area_of_rectangle():

    expected = 8
    rectangle = shapes.Rectangle()
    rectangle.width = 4
    rectangle.height = 2
    actual = rectangle.rectangle_area
    assert expected == actual

    expected = "Rectangle area with a width of 4 and height of 2 is 8"
    actual = str(rectangle)
    assert expected == actual

