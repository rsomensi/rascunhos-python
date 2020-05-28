#Crie um programa que leia um número inteiro pelo teclado e mostre a sua porção inteira.
import math
num = float(input('Typ a entire number: '))
print('The whole portion of {} is {}.'.format(num, math.trunc(num)))

