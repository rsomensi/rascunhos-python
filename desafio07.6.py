#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1 = R$ 3,27

wal = float(input('How many brazilian reais do you have in your wallet: '))
cot_dollar = 3.27

print('You can buy {:.2f} dollars!'.format(wal/cot_dollar))
