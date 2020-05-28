#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.

meters = float(input('How many meters: '))
cm = meters*100
mm = meters*1000

print('{:.2f} meters is equal to:\n{:.2f} centimeters\n{:.2f} mm.'.format(meters, cm, mm))
