from abc import ABC, abstractmethod


class Account:

    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    # @property
    # def agency(self):
    #     return self.agency
    #
    # @agency.setter
    # def agency(self, value):
    #     self._agency = value
    #
    # @property
    # def account(self):
    #     return self.account
    #
    # @account.setter
    # def account(self, value):
    #     self._account = value
    #
    # @property
    # def balance(self):
    #     return self.balance
    #
    # @balance.setter
    # def balance(self, value):
    #     self._balance = value

    """"Imprime detalhes da conta, extrato"""

    def details(self):
        print(f'Agência: {self.agency}', end=' ')
        print(f'Conta: {self.account}', end=' ')
        print(f'Saldo: {self.balance}')

    """deposit an amount of cash"""

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")
        self.balance += value
        self.details()

    @abstractmethod
    def withdraw(self):
        pass

