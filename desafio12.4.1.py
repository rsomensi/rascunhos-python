'''#Faça um programa que leia o ano de nascimento
#de um jovem, de acordo com a sua idade:
# - se ele ainda vai se alistar ao s.militar.
#-Se é a hora de se alistar.
#-Se já passou do tempo do alistamento.
#Deverá mostrar o tempo que falta ou que passou do prazo.'''

born = int(input('What year were you born: '))
from datetime import date
current_year = date.today().year
current_age = current_year - born
military_age = 18
print('We are in {} and you have {} years old!'.format(current_year, current_age))
if military_age > current_age:
    print('There still {} years to go before his military enlistment!\nYour enlistment will be in {}.'.format((military_age - current_age), (born + 18)))
elif military_age < current_age:
    print('{} years have passed since his military enlistment!\nEnlistment was in {}.'.format((current_age - military_age), (current_year - ((current_year - born) - military_age))))
else:
        print('Go to a military enlistment center this year!')
