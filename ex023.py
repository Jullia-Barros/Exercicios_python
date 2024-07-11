#Faça um programa  que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Por exemplo: Digite um número: 1834
# unidade: 4
# dezena:  3
# centena: 8
# milhar : 1
'''
num = input('Digite um número de 0 a 9999: ')
num = num.zfill(4)

print('Unidade é {}'.format(num[3]))
print('Dezena é {}'.format(num[2]))
print('Centena é {}'.format(num[1]))
print('Milhar é {}'.format(num[0]))
'''
# OUTRA FORMA DE SE FAZER
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10 # Divide o num por um e o resto da divisão por 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

