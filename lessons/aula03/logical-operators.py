# @file: logical-operators.py
# @author: Osvaldo Alves
# @date: 05/02/2023
# @description: learning to use the logical operators.

a = True   # boolean like 0 and 1 - True or False
b = False

if a == True :
    print('A variável \'A\' é verdadeira')
else :
    print('A variável \'A\' é falsa')

# boolean comparisons can be done with (int, float, str) 

if 1 == 1 : # Checks if one value is equal from another 
    print('1 é igual a 1.')
else :
    print('False')

if 'abacaxi' != 'banana' :  # Checks if one value is different from another
    print('\'abacaxi\' é diferente de \'banana\'.')
else :
    print('False')

if 10 > 5 : # Checks if one value is bigger from another
    print('10 é maior que 5')
else :
    print('False')

if 2 >= 2 : # Checks if one value is bigger or equal from another
    print('2 é maior ou igual a 2')
else :
    print('False')

if 5 < 10 : # Checks if one value is less from another
    print('5 é menor que 10')
else :
    print('False')

if 0.5 <= 1 :   # Checks if one value is less or equal from another
    print('0.5 é menor ou igual a 1')
else :
    print('False')