"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

"""
from oop_practice_basic_oper import BasicAccountOperation


class BankAccount(BasicAccountOperation):


    def update_info(self,owner):
        self.owner=owner



my_ac=BankAccount('IBAN1234','Ionut',4000)
my_ac.print_accountinfo()
my_ac.add_money(4000)
my_ac.print_accountinfo()
my_ac.withdrawn_money(9000)
my_ac.withdrawn_money(3000)
my_ac.update_info('John')
my_ac.print_accountinfo()






