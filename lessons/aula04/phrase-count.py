# @file: phrase-count.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: Exercise of phrase count.

# recieving the phrase
sentence = input('Digite uma frase: ')

# dividing the phrase in words
words = sentence.split()

# count the words
wordCout = len(words)

# showing result
print(f'A frase tem {wordCout}, palavra(s).')