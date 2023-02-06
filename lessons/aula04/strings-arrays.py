# @file: strings-arrays.py
# @author: Osvaldo Alves
# @date: 05/02/2023
# @description: Learning to use arrays in python.

phrase = 'Hello, world!'
print(phrase, '\n')

print(phrase.upper())
print(phrase.lower())
print(phrase.split(','))
print(phrase[0:5])
print('A frase tem ', phrase.count('l'), 'L\'s\n')
  
fair = ['banana','maçã','abacaxi','uva','melancia','morando','abacate'] 

print(fair)
print(fair[0:4])
print(fair[0:6:2])
fair.append('kiwi')
print(fair.count('uva'))
print(fair)
fair.remove('maçã')
print(fair)

