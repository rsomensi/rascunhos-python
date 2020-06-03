#Escreva um programa que leia os dois números
#inteiros e compare-os, mostrando na tela uma
#mensagem:
# - 0 primeiro valor é maior
# - 0 segundo valor é maior
# - Não existe valor maior, os dois são iguais.

n1 = int(input('Insert the first number: '))
n2 = int(input('Insert the second number: '))

if n1 > n2:
    print('The first number is greater!')
elif n2 > n1:
    print('The second number is greater!')
else:
    print('There is not greater value, both are equal!')
