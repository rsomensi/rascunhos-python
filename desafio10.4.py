#Desenvolva um programa que pergunte a
#distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando
# R$ 0,50 por KM para viagens de até 200km
#e R$0,45 para viagens mais longas.
km = float(input('Quantos KM foram rodados: '))
limit = 200
if km <= limit:
    s = km * 0.5
    print('O preço da passagem é R$ {:.2f}'.format(s))
else:
    i = km * 0.45
    print('O preço da passagem é R$ {:.2f}'.format(i))