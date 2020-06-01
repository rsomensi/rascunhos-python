#Escreva um programa para aprovar
# o empréstimo bancário para a compra
#de uma casa. O programa vai perguntar o
#valor da casa, o salário do comprador e
#em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo
#que ela não pode exceder 30% do salário ou
#então o empréstimo será negado.
print('-'*60)
print('\033[1;34m---SIMULADOR DE EMPRÉSTIMO--FINANCIAMENTO DA CASA PRÓPRIA---\033[m')
print('-'*60)
vlr_casa = float(input('Qual o valor da casa? '))
print('-'*60)
salario = float(input('Qual o seu salário mensal? '))
print('-'*60)
pgto = int(input('Em quantos meses você quer realizar o pagamento? '))
prest = vlr_casa/pgto
limit = (salario * 0.3)
print('-'*60)
print('A sua prestação mensal é de \033[1mR$ {:.2f}\033[m'.format(prest))
print('-'*60)
if prest > limit:
    print('A sua prestação representa {:.2f}% do seu salário!\nO limite permitido é R$ {:.2f}, equivalente a 30% do seu salário.\nStatus: \033[1;31mEMPRÉSTIMO NEGADO\033[m!!!'.format(((prest/salario)*100), limit))
else:
    print('A sua prestação representa {:.2f}% do seu salário!\nO limite permitido é R$ {:.2f}, equivalente a 30% do seu salário.\nStatus: \033[1;32mEMPRÉSTIMO APROVADO\033[m!!!'.format(((prest/salario)*100), limit))



