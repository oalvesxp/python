# @file: methods-functions.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: learning to use methods and functions.

def soma(a, b):
    value = a + b
    return value

value = soma(int(input('Primeiro valor: ')),int(input('Segundo valor: ')))
print(f'O valor da soma é de {value}')

def calcula_letras(arg):
    if len(arg) >= 7:
        print(f'A palavras tem 7 letras ou mais: {len(arg)}')
        return True
    else:
        print(f'A palavras tem menos de 7 letras: {len(arg)}')
        return False

print('\n')
item = calcula_letras(str(input('Digite o texto: ')))
print(item)