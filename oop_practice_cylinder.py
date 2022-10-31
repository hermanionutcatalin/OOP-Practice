"""
Class Cylinder, constructor height and radius
Methods:
    Volume
    Surface area
Testing with pytest

"""
import pytest
import math


class Cylinder:
    pi = math.pi

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return ((2 * Cylinder.pi * self.radius) * self.height) + ((Cylinder.pi * self.radius ** 2) * 2)


c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())

def test_surface_cylinder():
    assert c.surface_area()==94.24777960769379

def test_volume_cylinder():
    assert c.volume() == 56.548667764616276