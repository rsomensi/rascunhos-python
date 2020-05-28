#Faça um programa que leia 3 números e
#mostre qual é o maior e qual é o menor.

n1 = float(input('Typ a number: '))
n2 = float(input('Typ a number: '))
n3 = float(input('Typ a number: '))

list = [n1, n2, n3]

print('The greatest number is {}!'.format(max(list)))
print('The sort number is {}'.format(min(list)))