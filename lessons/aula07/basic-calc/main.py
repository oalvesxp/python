# @file: main.py
# @includes: src/soma.py src/sub.py src/mult.py src/div.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: Exercise of calculator with methods, functions and imports.

# imports
import src.soma
import src.sub
import src.mult
import src.div

# maths operations
soma = src.soma.soma(23, 56)
print(f'Resultado da soma: {soma}')

sub = src.sub.subtrai(58, 23)
print(f'Resultado da subtração: {sub}')

mult = src.mult.multiplica(9, 7)
print(f'Resultado da multiplicação: {mult}')

div = src.div.divide(32, 4)
print(f'Resultado da divisão: {div}')