#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angle = float(input('Typ a angle: '))
sin = math.sin(math.radians(angle))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angle, sin))
cos = math.cos(math.radians(angle))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angle, cos))
tan = math.tan(math.radians(angle))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angle, tan))