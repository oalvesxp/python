# @file: main.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: Exercise of calculator with methods, functions and imports.
# @use: ./main.py [args[1]].. [args[2]].. [args[3]]..
# @exemple: ./main.py multiplicar 8 9

#imports
import sys 
import src.methods

args = sys.argv
if (args[1] == 'somar'):
    value = src.methods.somar(float(args[2]), float(args[3]))
elif (args[1] == 'subtrair'):
    value = src.methods.subtrair(float(args[2]), float(args[3]))
elif (args[1] == 'multiplicar'):
    value = src.methods.multiplicar(float(args[2]), float(args[3]))
elif (args[1] == 'dividir'):
    value = src.methods.dividir(float(args[2]), float(args[3]))

print(value)