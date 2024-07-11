'''
Crie um programa que faça o computador jogar Jokempô com você
'''
import random
from random import choice
from time import sleep
print('\033[1;33m-=' * 15)
print(' Vou pensar!Tente adivinhar...')
print('-=' * 15, '\033[m')

lista = ['pedra', 'papel', 'tesoura']
jogador = str(input('Você quer pedra, papel ou tesora? '))
print('Jo')
sleep(0.3)
print('ken')
sleep(0.3)
print('po')
sleep(0.3)
computador = random.choice(lista)

if jogador == computador:
    print('\033[1;33mEmpate')
elif jogador == 'papel' and computador == 'pedra' or jogador == 'pedra' and computador == 'tesoura' or jogador == 'tesoura' and computador == 'papel':
    print('\33[1;32mVocê venceu\nJoguei {}'.format(computador))
else:
    print('\033[1;31mVocê perdeu\nJoguei {}'.format(computador))



