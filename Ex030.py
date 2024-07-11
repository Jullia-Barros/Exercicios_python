#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número: '))

if num % 2 == 0:        # % Módulo
    print('O número {}{}{} é par!'.format('\033[1;33m', num, '\033[m'))
else:
    print('O número {}{}{} é ímpar!'.format('\033[1;36m', num, '\033[m'))
