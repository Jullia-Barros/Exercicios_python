'''
Desenvolva um programa que leia o primeiro termo e a razão de um PA(Programação aritmetica).
No final, mostre os 10 primeiros termos dessa progressão.
'''
primTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos são: ')
for i in range(10):
    termo = primTermo + i * razao
    print(termo, end=' ')






