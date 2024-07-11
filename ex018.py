#Faça um progrma que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo.
'''
import math
angulo  = (float(input('Digite qual o valor do ângulo: ')))
angulo_em_radianos = math.radians(angulo)
seno    = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)
print('O seno de {:.0f} graus é {:.2f}\nCosseno de {:.0f} graus é {:.2f}'
      ' \nE a tangente de {:.0f} graus é {:.2f}'.format(angulo, seno, angulo, cosseno,angulo, tangente))
'''
# 2 forma de se fazer o exercício:
from math import radians, sin, cos, tan # Só utilizei os metodos radians, sin, cos, tan.
angulo = float(input('Digite o ângulo que você deseja: '))
seno   = sin(radians(angulo))               #radians vai converter o angulo em radianos
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))