# @file: menu-exercise.py
# @author: Osvaldo Alves
# @date: 05/02/2023
# @description: Exercise of logical operators and decision structures.

# Creating a 'menu' to pratice.

balance = 793.14
transfer01 = 83.15 
transfer02 = -459.99

print('Olá, selecione uma das opções a seguir:'
       + '\n    01 - Saldo da conta.'
       + '\n    02 - Fazer um pix.'
       + '\n    03 - Extrato da conta.\n')

option = input('Digite sua escolha: ')

if option == '01' :
    print('\nSeu saldo atual é de: R$',balance)
elif option == '02':
    pix = input('Insira a chave pix: ')
    value = input('Insira o valor a ser transferido: ')

    print('\nTransferência de R$',value, 'para a chave pix', pix, 'realizada com sucesso!')
elif option == '03' :
    print('Saldo atual: R$', balance, '\n')
    print(' 02 de fevereiro'
            + '\n quinta-feira'
            + '\n pix trasnf osvaldo02/02 R$', transfer01, '\n')
    print(' 31 de janeiro'
            + '\t erça-feira'
            + '\n pix trasnf osvaldo31/01 R$', transfer02)
else :
    print('Opção inválida, inicie o programa novamente.')