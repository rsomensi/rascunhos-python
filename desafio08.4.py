#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = str(input('Aluno 1 = '))
n2 = str(input('Aluno 2 = '))
n3 = str(input('Aluno 3 = '))
n4 = str(input('Aluno 4 = '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))






