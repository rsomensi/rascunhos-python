#Escreva um programa que faça o computador
#"pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
from random import randint

n = randint(0, 5)
c = int(input('Digite um número entre 0 e 5: '))
print('O número sorteado foi {}'.format(n))
if n == c:
    print('Você ACERTOU!!!')
else:
    print('Tente novamente!')

