"""
Class Rectangle, constructor lenght, witd, color
Methods:
    Describe
    Area
    Perimeter
    Change color
Pytest Unit Testing

"""

class Rectangle:
    # lenght and width integers, color is string

    def __init__(self, lenght, width, color):
        self.lenght = lenght
        self.width = width
        self.color = color

    def describe_rectangle(self):
        print(self.color)
        print(self.lenght)
        print(self.width)

    def area_rectangle(self):
        return self.lenght * self.width

    def perimeter_rectangle(self):
        return 2 * self.lenght + 2 * self.width

    def change_color(self, new_color):
        self.color = new_color


my_rectangle = Rectangle(10, 5, 'red')
my_rectangle.describe_rectangle()
print(my_rectangle.area_rectangle())
print(my_rectangle.perimeter_rectangle())
my_rectangle.change_color('green')
my_rectangle.describe_rectangle()

# def test_rectangle_color_change():
#     assert my_rectangle.color=='green'
#
# def test_rectangle_perimeter():
#     assert my_rectangle.perimeter_rectangle()==30
#
# def test_rectangle_area():
#     assert my_rectangle.area_rectangle()==50