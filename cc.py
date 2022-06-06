from account import Account


class Current(Account):

    def __init__(self, extra_limit, agency, account, balance):
        super().__init__(agency, account, balance)
        self._extra_limit = extra_limit

    @property
    def extra_limit(self):
        return self._extra_limit

    def withdraw(self, value):
        if not isinstance(value, (int, float)):
            raise print('Valor nao é numerico')

        if (self.balance + self.extra_limit) < value:
            print('Insufficient balance on account')
            self.details()
            return

        self.balance -= value
        self.details()
