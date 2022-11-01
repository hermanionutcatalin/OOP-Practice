"""
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
"""

from oop_pilons_practice.oop_abstraction_encapsulation import FormaGeometrica


class Square(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def geometric_area(self):
        return self.__latura ** 2

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter Latura noua este {latura}')
        self.__latura=latura

    @latura.deleter
    def latura(self):
        print(f'Deleter Latura')
        self.__latura=None

if __name__ == '__main__':
    my_patrat=Square(10)
    my_patrat.latura=11
    my_patrat.latura
    del my_patrat.latura
    my_patrat.latura




