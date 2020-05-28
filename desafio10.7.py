#Escreva um programa que pergunte o salário
#de um funcionário e calcule o valor do seu
#aumento.
#Para salários superiores a R$ 1.250,00,
#calcule aumento de 10%.
#Para os inferiores ou iguais, o aumento é de
#15%.
sal = float(input('Digite o seu salário em R$: '))
if sal > 1250:
    print('Seu salário recebeu um aumento de 10%! Agora você receberá {}'.format(sal+(sal*0.10)))
else:
    print('Seu salário recebeu um aumento de 15%! Agora você receberá {}'.format(sal+(sal*0.15)))