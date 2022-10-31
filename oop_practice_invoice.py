"""
Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""
from datetime import datetime
from texttable import Texttable


class Invoice:
    serial = 'INV123'

    def __init__(self, inv_num, inv_prod, inv_qty, inv_price):
        self.inv_num = inv_num
        self.inv_prod = inv_prod
        self.inv_qty = inv_qty
        self.inv_price = inv_price

    def change_inv_quantity(self, inv_qty_new):
        self.inv_qty = inv_qty_new

    def change_inv_price(self, inv_price_new):
        self.inv_price = inv_price_new

    def change_inv_prod(self, inv_prod_new):
        self.inv_prod = inv_prod_new

    def generate_inv(self):
        t = Texttable()
        z = Texttable()
        t.add_rows(
            [['Serie', 'Numar', 'Data'], [Invoice.serial, self.inv_num, datetime.today()]])

        z.add_rows([['Produs', 'Cantitate', 'Pret', 'Total'],
                    [self.inv_prod, self.inv_qty, self.inv_price, self.inv_qty * self.inv_price]])

        print(t.draw())
        print(z.draw())


my_invoice = Invoice(1234, 'Xperia', 100, 100)
print(my_invoice.generate_inv())
my_invoice.change_inv_price(10)
my_invoice.change_inv_prod('Nokia')
my_invoice.change_inv_quantity(50)
print(my_invoice.generate_inv())
