"""
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
"""

from oop_pilons_practice.oop_abstraction_encapsulation import FormaGeometrica


class Circle(FormaGeometrica):

    def __init__(self, raza):
        self.__raza=raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter Raza noua este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter Raza')
        self.__raza = None

    def geometric_area(self):
        return self.pi * self.__raza ** 2

    def geometric_description(self):
        print('Eu nu am colturi')

"""
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

"""
if __name__ == '__main__':
    my_circle=Circle(2)
    print(my_circle.geometric_area())
    my_circle.raza
    my_circle.raza=12
    my_circle.raza
