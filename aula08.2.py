#usando função FROM

from math import sqrt, floor
num1 = int(input('Typ a number: '))
sr1 = sqrt(num1)
print('The square root of {:.2f} is equal to {:.2f}.'.format(num1, floor(sr1)))