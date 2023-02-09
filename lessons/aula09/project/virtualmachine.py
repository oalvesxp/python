# @project: infra-calculator @author: Osvaldo Alves @date: 08/02/2023
# @description: Virtual machine object.

from resources import *

class vm(VCPU, RAM, HDD):
    def __init__(self, vcpu, ram, hdd):
        VCPU.__init__(self, vcpu)
        RAM.__init__(self, ram)
        HDD.__init__(self, hdd)