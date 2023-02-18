# @project: infra-calculator @author: Osvaldo Alves @date: 08/02/2023
# @description: Virtual Machine calculator.

from virtualmachine import *

print('Selecione uma das opções abaixo:')
while True:
    print('1. Calcular Virtual Machine')
    print('2. Sair')

    option = int(input('Digite a opção: '))

    if option == 1:
        print('')
        
        name = str(input('Qual o nome da VM: '))
        vcpu = int(input('vCPU: '))
        ram = int(input('RAM (GB): '))
        hdd = int(input('HDD (GB): '))
        
        machine = vm(vcpu, ram, hdd)
        print(f'\nHostname: {name} - {vcpu}vCPU, {ram}GB, {hdd}GB')
        print(f'O total é de R$ {machine.calc_vcpu() + machine.calc_ram() + machine.calc_hdd()}\n')
    elif option == 2:
        break
    else:
        print('')
        print('Valor inválido!\n')