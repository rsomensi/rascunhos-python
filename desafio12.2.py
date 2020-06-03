#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#- 1 para binário
#- 2 para octal
#- 3 para hexadecimal

num = int(input('Insert a integer number: '))
print('''Choose a option:
[1] convert to BINARY
[2] convert to OCTAL
[3] convert to HEXADECIMAL''')
choice = int(input('What is your choice? '))

if choice == 1:
    print('{} convert to BINARY is equal to {}'.format(num, bin(num)[2:]))
elif choice == 2:
    print('{} convert to OCTAL is equal to {}'.format(num, oct(num)[2:]))
elif choice == 3:
    print('{} convert to HEXADECIMAL is equal to {}'.format(num, hex(num)[2:]))
else:
    print('Invalid option.')