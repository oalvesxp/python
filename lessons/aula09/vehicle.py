# @file: vehicle.py
# @author: Osvaldo Alves
# @date: 07/02/2023
# @description: Object vehicle.

class Vehicle:
    def __init__(self, brand, model, color, wheels, fuelTank, fuel):
        self.brand = brand
        self.model = model
        self.color = color
        self.wheels = wheels
        self.fuelTank = fuelTank
        self.fuel = fuel
    
    def toFuel(self, gas):
        self.fuel += gas