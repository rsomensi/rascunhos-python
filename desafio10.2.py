#Escreva um programa que leia a velocidade
# de um carro.
#Se ele ultrapassar 80km/h, mostre uma men-
#sagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km
#acima do limite.
vel = int(input('Velocidade auferida: '))
limit = 80
multa = (vel - limit)*7
if vel <= limit:
    print('Boa viagem!!!')
else:
    print('VOCÊ FOI MULTADO.\nO valor da sua multa é R$ {:.2f}'.format(multa))