# @file: bank-account.py
# @author: Osvaldo Alves
# @date: 05/02/2023
# @description: Bank account system with class and methonds to deposit, withdraw and check balance.
# @more: I perfected the account system, making the user have to interact to carry out the operations.

class accounts :
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, value) :
        self.balance += value
        print('Depósito de R$', value, 'realizado com sucesso.')
        print('Saldo atual: R$', self.balance, '\n')

    def withdraw(self, value) :
        if self.balance < value :
            print('Saldo insuficiente para realizar a operação.\n')
        else :
            self.balance -= value
            print('Saque de R$', value, 'realizado com sucesso.')
            print('Saldo atual: R$', self.balance, '\n')

    def extract(self) :
        print('Nome:', self.name, '\nSaldo: R$', self.balance,'\n')

##  Test the account and functions
#account = accounts('Osvaldo Alves')
#account.deposit(246.90)
#account.extract()
#account.withdraw(750)

account = accounts(
    input('Insira o mome do titular: '),
)

while True:
    print('\n Opções:')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Ver saldo')
    print('4. Sair\n')

    option = int(input('Escolha uma opção: '))

    if option == 1 :
        value = float(input('Qual o valor do depósito? R$ '))
        account.deposit(value)
    elif option == 2 :
        value = float(input('Qual o valor do saque? R$ '))
        account.withdraw(value)
    elif option == 3 :
        account.extract()
    elif option == 4 :
        break
    else :
        print('Opção inválida.')