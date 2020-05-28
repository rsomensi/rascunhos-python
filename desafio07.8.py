#Faça um algoritmo que leia ao preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Price of car: '))
discount = 0.05

print('Discount value: {:.2f}\nTotal value with 5% off: {:.2f}'.format((p*discount), (p-(p*discount))))




