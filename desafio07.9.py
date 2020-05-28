#Faço um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('What is your salary? '))
rate_of_increase = 0.15

print('Your new salary is {} dollars!\nYou got an increase of {} dollars!!!'.format(salary+(salary*rate_of_increase), salary*rate_of_increase))
