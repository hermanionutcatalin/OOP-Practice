"""
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

from oop_inhertitance_abst_encap import Square
from oop_circle_encapsulation_abstract import Circle

if __name__ == '__main__':

    my_patrat=Square(2)
    my_circle=Circle(2)

    my_patrat.geometric_description()
    my_circle.geometric_description()