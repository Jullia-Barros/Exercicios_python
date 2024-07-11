#Crie um programa que leia um número real e mostre na tela a sua parte inteira.
#Exemplo: Digite um número: 6.124... O número 6.127 tem a parte inteira 6.
'''
1 forma de fazer:
num = float(input('Digite um número: '))
print('O número {} tem como parte inteira {:.0f}.'.format(num, num))
'''
'''
2 forma de se fazer o exercicio:
from math import trunc
num = (float(input('Digite um valor: ')))
print('O valor digitado é {} e a sua parte intera é {}'.format(num, trunc(num))) # Esse TRUNC vai cortar a parte intera do num.
'''

# 3 forma de se fazer o exercício:
num = float(input('Digite um valor: '))
print('O valor digitado é {} e sua parte intera é {}'.format(num, int(num)))