""""
Simple Class Circle creation, constructor of radius and color
Methods:
Describe
Area
Diameter
Circumference
Pytest Unit testing
"""
import pytest
import math


class Circle:
    pi = math.pi

    # radius=integer, color= string

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def describe_circle(self):
        print(self.radius)
        print(self.color)

    def area_circle(self):
        return Circle.pi * self.radius ** 2

    def diameter_circle(self):
        return self.radius * 2

    def circumferernce_circle(self):
        return 2 * Circle.pi * self.radius


my_circle = Circle(10, 'red')
my_circle.describe_circle()
print(my_circle.area_circle())
print(my_circle.diameter_circle())
print(my_circle.circumferernce_circle())


# def test_circumference_circle():
#     assert (my_circle.circumferernce_circle()) == 62.83185307179586
#
# def test_area_circle():
#     assert (my_circle.area_circle()) == 314.1592653589793
#
# def test_diamter_circle():
#     assert (my_circle.diameter_circle()) == 20