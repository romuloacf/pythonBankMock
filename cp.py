from account import Account


class Poup(Account):

    def withdraw(self, value):
        if not isinstance(value, (int, float)):
            raise print('Valor nao é numerico')

        if self.balance < value:
            print('Insuficient balance on account')

        self.balance -= value
        self.details()

