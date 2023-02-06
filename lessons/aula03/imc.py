# @file: imc.py
# @author: Osvaldo Alves
# @date: 05/02/2023
# @description: IMC Calculator.

# input values to calc. Converting the 'str' to 'float'
weight = float(input('Insira o seu peso: '))
height = float(input('Insira a sua altura: '))

# calculating the IMC
    # wight / height ^ 2
imc = weight / (height ** 2)
print('IMC =', imc)

# answers to user
if imc <= 18.5 :
    print('\nVocê está abaixo do peso.')
elif 18.6 <= imc and imc <= 24.9 :
    print('\nVocê está no peso ideal.')
elif 25.0 <= imc and imc <= 29.9 :
    print('\nVocê está com sobrepeso.')
elif 30.0 <= imc and imc <= 34.9 :
    print('\nVocê está com obesidade de grau I.')
elif 35.0 <= imc and imc <= 39.9 :
    print('\nVocê está com obesidade de grau II.')
elif 40 <= imc :
    print('\nVocê está com obesidade de grau III.')