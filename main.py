from bank import  Bank
from client import Client
from account import Account
from cp import Poup
from cc import Current


banco = Bank()

client1 = Client('Luiz', 30)
client2 = Client('Maria', 18)
client3 = Client('João', 50)

account1 = Poup(1111, 254136, 0)
account2 = Poup(2222, 254137, 0)
account3 = Poup(1212, 254138, 0)

client1.insert_account(account1)
client2.insert_account(account3)
client3.insert_account(account3)

banco.insert_client(client1)
banco.inset_account(account1)

if banco.authentincate(client1):
    client1.account.deposit(0)
    client1.account.withdraw(20)
else:
    print('Cliente não autenticado.')

print('####################')
