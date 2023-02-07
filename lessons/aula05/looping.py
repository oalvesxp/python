# @file: loopings.py
# @author: Osvaldo Alves
# @date: 06/02/2023
# @description: Learning to use loopings.

fair = ['Abacaxi','Mamão','Abacate','Maçã','Melancia','Uva','Laranja']
#for i in fair :
#    print(i)

for i in range(4) :
    print(fair[i])

print('\n')
for i in range(len(fair)) :
    print(fair[i])

#for i in range(1, 11) :
#    print(i)

i = 1
while i < 11 :
    print(i)
    i += 1


count = 0
for fruit in fair :
    count += 1

print(count)

c = 0
while True:
    c += 1
    if c == 15:
        print(c)
        break
