#Crie um programa que leia o nome de
#uma pessoa e diga se ela tem SILVA no nome.
nome = str(input('Escreva seu nome completo: ')).strip()
print("O nome tem Silva na sua composição? {}".format('SILVA' in nome.upper()))
