# @file: output-file.py @author: Osvaldo Alves @date: 09/02/2023
# @description: Learning to create, write and read external files from sytem.

# args:
    # r --> read (only if file exist)
    # w --> write (if the file isn't exist it creates it) - replace the content
    # r+ --> read and write (if the file isn't exist it creates it)
    # a --> write (if the file isn't exist it creates it) - append the content
    # b --> binary mode

file = open('output-file.log','a')
file.write('Hello world!\n')

for i in range(1,16):
    file.write(f'{i} - Hello world!\n')

file = open('output-file.log','r')
print(file.read())

image = open('logo.png', 'rb')
print(image.read())