"""
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

"""
import math
from abc import abstractmethod


class FormaGeometrica:
    pi=math.pi

    @abstractmethod
    def geometric_area(self):
        raise NotImplementedError

    def geometric_description(self):
        print('Cel mai probabil am colturi')



