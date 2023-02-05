# @file: decision-structures.py
# @author: Osvaldo Alves
# @date: 05/02/2023
# @description: learning to use the logical operators in decision structures.

a = 7
b = 5
c = a * b
d = a ** b

print(a, 'x', b, '=', c)
print(a, '^', b, '=', d, '\n')

# boolean with two conditions with 'and'
    # true and true = true
    # false and true = false
    # true and false = false
    # false and false = false

print('Comparando se \'c\' e \'d\' são verdadeiros ou falsos.')
if c == 35 and d > 16000 :
    print('\'c\' é igual a', c)
    print('\'d\' é maior que 16000.\n')
else :
    print('Umas das opções são inválidas.\n')

# boolean with two conditions with 'or'
    # true of true = true
    # false of true = true
    # true or false = true
    # false or false = false
print('Comparando se \'c\' ou \'d\' são verdadeiros ou falsos.')
if c == 35 or d < 16000 :
    print('\'c\' é igual a', c, 'ou \'d\' é maior que 16000.')
    print('\'d\' é maior que 16000.')
else :
    print('As duas opções são inválidas.')