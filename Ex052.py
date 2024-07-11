'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
Divisiveis por 1 e por ele mesmo

num = int(input('Digite um número: '))
if num % 3 == 0 and num % 2 != 0:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))
'''
num = int(input('Digite um número: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1;32m', end=' ')
        total += 1
    else:
        print('\033[1;31m', end=' ')
    print(i, end=' ')
if total == 2:
    print('\nO número {} é primo'.format(num))
else:
    print('\nO número {} não é primo'.format(num))








