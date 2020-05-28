#O professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
#a ordem sorteada
import random
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
sel = [n1, n2, n3, n4]
random.shuffle(sel)
print('A ordem de apresentação será:')
print(sel)

