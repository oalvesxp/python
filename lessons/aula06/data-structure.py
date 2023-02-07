# @file: data-structure.py
# @author: Osvaldo Alves
# @date: 06/02/2023
# @description: Learning to use list, dict, tuple and set.

myList = ['João', 'Maria']  # list: With index, items do repeat
myTuple = ('Feijão', 'Arroz')   # tuple: Not dynamic
myDict = {'nome':'Osvaldo', 'idade': 26} # dict: Hash table, like object json
mySet = {'Osvaldo', 'João'} # set: Items do not repeat. Without index

print(type(myList))
print(type(myTuple))
print(type(myDict))
print(type(mySet))

if 'Osvaldo' in myDict.values() :
    print(myDict['nome'], 'está presente no dicionário e ele tem', myDict['idade'], 'anos de idade')

myDict['sexo'] = 'masculino'
myDict['endereco'] = 'Rua João das Neves'
print(myDict)

# empty
lista = []
tupla = ()
dicionario = {}
conjunto = set()