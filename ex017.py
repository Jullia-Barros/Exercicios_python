#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo,
#calcule e mostre o comprimento da hipotenusa.
#Fórmula para calcular triângulos retângulo: c² = a² + b²
#Para encontrar o valor de c, a hipotenusa, tiramos a raiz quadrada de ambos os lados:
#c = raiz de c
'''
import math
catOposto = float(input('Digite o lado do cateto oposto: '))
catAdjacente = float(input('Digite o lado do cateto adjacente: '))
hipotenusa = math.sqrt(catOposto ** 2 + catAdjacente ** 2)
print('O valor da hipotenusa será de {:.2f}!'. format(hipotenusa))


import math

#Outra maneira de fazer o exercício sem importção da biblioteca math!
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
#3 maneira de se fazer:
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

