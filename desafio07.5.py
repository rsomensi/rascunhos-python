#Escreva um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

mult = int(input('Insert multiplier: '))
''''print('-'*15)
print('{} x {:2} = {}'.format(mult, 1, mult*1))
print('{} x {:2} = {}'.format(mult, 2, mult*2))
print('{} x {:2} = {}'.format(mult, 3, mult*3))
print('{} x {:2} = {}'.format(mult, 4, mult*4))
print('{} x {:2} = {}'.format(mult, 5, mult*5))
print('{} x {:2} = {}'.format(mult, 6, mult*6))
print('{} x {:2} = {}'.format(mult, 7, mult*7))
print('{} x {:2} = {}'.format(mult, 8, mult*8))
print('{} x {:2} = {}'.format(mult, 9, mult*9))
print('{} x {:2} = {}'.format(mult, 10, mult*10))
print('-'*15)'''''
x = 0
while x < 11:
    print('{} X {:2} = {}'.format(x, mult, (x * mult)))
    x += 1