#Crie um programa que leia duas notas de um aluno e calcule
#sua média, mostrando uma mensagem ao final, de acordo com a mèdia.
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

t1 = float(input('Insert the first score: '))
t2 = float(input('Insert the second score: '))
school_average = (t1 + t2)/2
if school_average < 5.0:
    print('You have failed!')
elif school_average > 5.0 and school_average < 7.0:
    print('You are recovering from school!')
else:
    print('Congratulations, you have been approved!!!')
