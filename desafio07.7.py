#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

width = float(input('What is the width of the wall: '))
height = float(input('What is the height of the wall: '))
wall_area = width * height

print('The wall area is: {:.2f}m²\nYou will need {:.2f} liters of paint to paint the wall!'.format(wall_area, (wall_area/2)))



