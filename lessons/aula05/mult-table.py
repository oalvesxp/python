# @file: mult-table.py
# @author: Osvaldo Alves
# @date: 06/02/2023
# @description: Multiplication table with loopings.

for i in range(1, 11):
    for c in range(1, 11):
        print(f'{i} x {c} =', i*c)
    print('\n')