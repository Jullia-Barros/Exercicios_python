#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep                          #Apenas importando o método sleep

print('\033[1;33m-=-' * 17)
print('Vou pensar em um número de 0 a 5.Tente adivinhar...')
print('-=-' * 17, '\033[m')

num = randint(0,5)
tentativa = int(input('\033[1;34mDigite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)                                        #Computador vai esperar 3 segundos!
if tentativa == num:
    print('\033[1;32mVocê venceu!')
else:
    print('\033[1;31mPoxa, vc perdeu pra uma máquina\nO número era {}!'.format(num))



