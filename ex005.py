#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o antecessor.
"""num = int(input('Digite um número: '))
suc = num - 1
ant = num + 1
print('Você digitou o número {}'.format(num))
print('O sucessor é {}'.format(suc))
print('É seu antecessor é {}'.format(ant))
"""
# Posso fazer também usando só 1 variável, já que o programa acaba quando mostre o antecessor e o sucessor!

num = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(num, num-1, num+1))

#Quanto menos vc utilizar variável, mas mémoria vc economiza!