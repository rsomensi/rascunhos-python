#Desenvolva um programa que leio o compri-
#mento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

triang = (r1 + r2) > r3
triang2 = (r2 + r3) > r1
triang3 = (r3 + r1) > r2

if triang and triang2 and triang3 is True:
    print('As suas três retas \033[1;32mPODEM FORMAR\033[m um triângulo!!!')
else:
    print('As suas retas \033[1;31mNÃO PODEM\033[m formar um triângulo!!!')
