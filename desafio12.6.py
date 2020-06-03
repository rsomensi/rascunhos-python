#Leia o ano de nascimento de um atleta e mostre sua categoria.
#Até 9 anos: MIRIM
#Até 14 anos:INFANTIL
#Até 19 anos:JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

y_born = int(input('Year you were born: '))
from datetime import date
current_y = date.today().year
current_age = current_y - y_born
print('You have {} years old.'.format(current_age))
if current_age <= 9:
    print('Child category 1.')
elif current_age <= 14:
    print('Child category 2.')
elif current_age <= 19:
    print('Junior category.')
elif current_age <= 25:
    print('Senior category.')
else:
    print('Master category.')