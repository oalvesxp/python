# @file: main.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: Practicing the orientation to object.

from car import Car

carro = Car('Ford', 'New Fiesta SE 1.6 16V','Black', 54, 10)
print('Marca: ',carro.brand)
print('Modelo: ', carro.model)
print('Cor: ', carro.color)
print('Tanque de combustível (L): ', carro.fuelTank)
print('Combustível (L): ', carro.fuel)

print('')
carro.toFuel(30)
print(f'Combustível no tanque: {carro.fuel} L')