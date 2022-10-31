class BasicAccountOperation:

    def __init__(self, iban, owner, balance):
        self.iban = iban
        self.owner = owner
        self.balance = balance

    def add_money(self,amount):
        self.balance=self.balance+amount

    def withdrawn_money(self, amount):
        if self.balance>amount:
            self.balance=self.balance-amount
        else:
            print('Insufficient funds')

    def print_accountinfo(self):
        print(self.iban)
        print(self.owner)
        print(self.balance)