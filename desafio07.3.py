#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

test1 = float(input('Test 1: '))
test2 = float(input('Test 2: '))
school_average = (test1+test2)/2

print('The average between {:.1f} and {:.1f} is {:.1f}'.format(test1, test2, school_average))

