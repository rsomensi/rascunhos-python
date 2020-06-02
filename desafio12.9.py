'''Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento:
-à vista: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros'''

price = float(input('Insert the full price: '))
payment_type = str(input('Choose a payment:\n1 - in cash;\n2 - Credit card 1x;\n3 - Credit card 2x;\n4 - Credit card 3x or more.\nPayment code: '))

if payment_type == '1':
    print('With this payment condition the value of the product will be \033[1m$ {:.2f}\033[m.'.format(price - (price * 0.10)))
elif payment_type == '2':
    print('With this payment condition the value of the product will be \033[1m$ {:.2f}\033[m.'.format(price - (price * 0.05)))
elif payment_type == '3':
    print('With this payment condition the value of the product will be \033[1m$ {:.2f}\033[m.'.format(price))
elif payment_type == '4':
    print('With this payment condition the value of the product will be \033[1m$ {:.2f}\033[m.'.format(price + (price * 0.20)))
else:
    print("\033[31mPlease, choose an available payment method!\033[m")