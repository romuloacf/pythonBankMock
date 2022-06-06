class Bank:

    def __init__(self):
        self.agency = [1111, 2222, 3333]
        self.clients = []
        self.accounts = []

    def insert_client(self, client):
        self.clients.append(client)

    def inset_account(self, account):
        self.accounts.append(account)

    def authentincate(self, client):
        if client not in self.clients:
            return False
        if client.account not in self.accounts:
            return False
        if client.account.agency not in self.agency:
            return False

        return True
