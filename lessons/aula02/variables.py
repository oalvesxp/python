# @file: variables.py
# @author: Osvaldo Alves
# @date: 03/02/2023
# @description: learning to creating variables to print on terminal.

name = 'Osvaldo Alves'
age = 26
height = 1.79

print(name, type(name)) #printing 'name / age / height' and debugging variable type
print(age, type(age))
print(height, type(height), '\n')

print(name, 'tem', age, 'anos e', height, 'de altura.') #printing a sentence with the variables created using ',' to concatenate 'str' with 'int' and 'float'