# @project: infra-calculator @author: Osvaldo Alves @date: 08/02/2023
# @description: resources from virtual machine.

class VCPU:
    def __init__(self, vcpu):
        self.vcpu = vcpu
    
    def calc_vcpu(self):
        if 1 <= self.vcpu <= 2:
            return float(90 * self.vcpu)
        elif 3 <= self.vcpu <= 5:
            return float(80 * self.vcpu)
        elif 6 <= self.vcpu <= 10:
            return float(70 * self.vcpu)
        elif 11 <= self.vcpu <= 40:
            return float(60 * self.vcpu)
        else:
            return float(45 * self.vcpu)

class RAM:
    def __init__(self, ram):
        self.ram = ram
    
    def calc_ram(self):
        if 1 <= self.ram <= 6:
            return float(80 * self.ram)
        elif 7 <= self.ram <= 14:
            return float(70 * self.ram)
        elif 15 <= self.ram <= 49:
            return float(60 * self.ram)
        else:
            return float(45 * self.ram)

class HDD:
    def __init__(self, hdd):
        self.hdd = hdd
    
    def calc_hdd(self):
        if 1 <= self.hdd <= 100:
            return float(2 * self.hdd)
        elif 101 <= self.hdd <= 500:
            return float(1.60 * self.hdd)
        elif 501 <= self.hdd <= 999:
            return float(1.30 * self.hdd)
        else:
            return float(1.15 * self.hdd)