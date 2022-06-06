from person import Person


class Client(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None
        # self._account = None

    def insert_account(self, account):
        self.account = account


