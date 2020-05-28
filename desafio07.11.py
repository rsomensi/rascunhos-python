#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

dias = float(input('How many days did the rental last: '))
km = float(input('How many kilometers did the car go: '))

print('The total payable is R${:.2f}'.format((dias*60)+(km*0.15)))