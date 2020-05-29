#Escreva um programa que leia a velocidade
# de um carro.
#Se ele ultrapassar 80km/h, mostre uma men-
#sagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km
#acima do limite.
vel = float(input('Velocidade auferida: '))
limit = 80
multa = (vel - limit)*7
if vel <= limit:
    print('\033[1;32m-Ok-\033[m' * 30)
    print('\033[1;40;32mBoa viagem!!!\033[m')
    print('\033[1;32m-Ok-\033[m' * 30)
else:
    print("\033[1;31m-X-\033[m" * 30)
    print('\033[1;31;40mVOCÊ FOI MULTADO.\033[m\n\033[1;31;40mO valor da sua multa é R$ {:.2f}\033[m'.format(multa))
    print('\033[1;31m-X-\033[m' * 30)