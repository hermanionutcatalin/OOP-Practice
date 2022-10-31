"""
Class Line, constructor is containing the coordinate of two points
Methods:
    Distance between points
    Slope

Pytest Unit Testing
"""
import pytest
import math


class Line:
    # coordinate 1 and 2 are tuples format
    def __init__(self, coordinate1, coordinate2):
        self.point1 = coordinate1
        self.point2 = coordinate2

    def distance(self):
        return math.dist(self.point1, self.point2)

    def slope(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        if (x1 - x2) != 0:
            return ((y1 - y2) / (x1 - x2))
        else:
            print('Fatal error, 0 division')


li = Line((3, 2), (8, 10))
print(li.distance())
print(li.slope())

# def testing_line_slope():
#     assert li.slope()==1.6
#
# def testing_division():
#     assert li.point1[1]-li.point2[1]!=0
#
# def testing_line_distance():
#     assert li.distance()==9.433981132056603

