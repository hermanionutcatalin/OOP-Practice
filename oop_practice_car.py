"""
Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
Pytest Unit Testing
"""



class Car:
    mark = 'Dacia'
    act_speed = 0
    color = 'Grey'
    available_color = ('Red', 'Bleu', 'Black', 'White')
    registr = False

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def car_description(self):
        print(
            f"Marca{self.mark}\nModel {self.model}\nCuloare {self.color}\nInmatrirculata {self.registr}\nViteza maxima {self.max_speed} km/h\nViteza Actuala {self.act_speed} km/h")

    def car_registration(self):
        self.registr = True

    def car_paint(self, new_color):
        available = list(self.available_color)
        for i in range(0, len(available)):
            available[i] = available[i].lower()
        if new_color.lower() in available:
            self.color = new_color
        else:
            print('Color not available for paint')

    def car_accelerate(self, give_speed):
        if give_speed <= 0:
            print('Error, cannot accelerate below or equal 0 km/h')
        elif give_speed > 0 and give_speed <= self.max_speed:
            self.act_speed = give_speed
            print(f'Car accelerating to {self.act_speed} km/h')
        else:
            print(f'Car accelerating to {self.max_speed} ')

    def car_stop(self):
        self.act_speed = 0
        print('Car stoping')


my_car = Car('Logan', 160)
my_car.car_description()
my_car.car_paint('red')
my_car.car_accelerate(100)
my_car.car_stop()
my_car.car_accelerate(100)
my_car.car_description()

# def test_my_car_accelerate_stop():
#     assert my_car.act_speed == 100
#
# def test_my_car_stop():
#     my_car.car_stop()
#     assert my_car.act_speed == 0
#
# def test_unavailable_color():
#     assert my_car.car_paint('xdx')==None
#
# def test_my_car_color():
#     assert my_car.color == 'red'


