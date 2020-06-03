#Refaça o desafio dos triângulos.
#Acrescente o recurso para exibir o tipo de triângulo.
#-Equilatero = todos os lados iguais
#-Isósceles = dois lados iguais
#-Escaleno = todos os lados diferentes
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

triang = (r1 + r2) > r3
triang2 = (r2 + r3) > r1
triang3 = (r3 + r1) > r2

if triang and triang2 and triang3 is True:
    print('As suas três retas \033[1;32mPODEM FORMAR\033[m um triângulo!!!')
    if r1 != r2 != r3 != r1:
        print('Trata-se de um triângulo ESCALENO.')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r3 != r2 or r3 == r2 and r2 != r1:
        print('Trata-se de um triângulo ISÓCELES.')
    elif r1 == r2 == r3:
        print('Trata-se de um triângulo EQUILATERO.')
else:
    print('As suas retas \033[1;31mNÃO PODEM\033[m formar um triângulo!!!')