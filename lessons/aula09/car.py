# @file: vehicle.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: Object vehicle.
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, color, fuelTank, fuel):
        Vehicle.__init__(self, brand, model, color, 4, fuelTank, fuel)
    
    def toFuel(self, gas):
        limit = self.fuelTank - self.fuel
        if gas < limit:
            self.fuel += gas
            print('Abastecimento realizado com sucesso!')            
            return self.fuel
        elif gas > limit:
            self.fuel += limit
            print('Tanque cheio!')
            return self.fuel
