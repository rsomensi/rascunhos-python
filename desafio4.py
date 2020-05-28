#Faça um programa que leia pelo teclado e emostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

test1 = input('Typ something: ')
print('O tipo primitivo desse valor = ', type(test1))
if(test1.isalpha()):
    print('Test1 is alpha!')
else:
    print('Is not alpha!')

if(test1.isalnum()):
    print('Test1 is alnumc!')
else:
    print('Is not alnum!')

if(test1.isascii()):
    print('Test1 is ascii!')
else:
    print('Is not ascii!')

if(test1.isdecimal()):
    print('Test1 is decimal!')
else:
    print('Is not decimal!')

if(test1.isdigit()):
    print('Test1 is digit!')
else:
    print('Is not digit!')

if(test1.isidentifier()):
    print('Test1 is identifier!')
else:
    print('Is not identifier!')

if(test1.islower()):
    print('Test1 is lower!')
else:
    print('Is not lower!')

if(test1.isprintable()):
    print('Test1 is printable!')
else:
    print('Is not printable!')

if(test1.istitle()):
    print('Test1 is title!')
else:
    print('Is not title!')

if(test1.isupper()):
    print('Test1 is upper!')
else:
    print('Is not upper!')

if(test1.isspace()):
    print('Test1 is space!')
else:
    print('Is not space!')

if(test1.isnumeric()):
    print('Test1 is numeric!')
else:
    print('Is not numeric!')