'''
Melhore o jogo do desafio 028 onde o compuatdor vai 'pensar' em um num entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer
..Parabens vc acertou depois de {} alternativas.
'''
from random import randint

print('\033[1;33m', '-=' * 21)
print('\033[1;33m Vou pensar em um número.Tente adivinhar!')
print('-=' * 21, '\033[m')

computador = randint(0, 10)
jogador = 0
tentativas = 0

while computador != jogador:
    jogador = int(input('Digite um número de 0 a 10: '))
    if computador == jogador:
        tentativas = jogador + 1
        print('\033[1;32mVocê venceu\033[m')
        print('Parabéns, vc acertou depois de {} tentativas'.format(tentativas))
    else:
        print('\033[1;31mVocê perdeu, pensei no número {} \033[m'.format(computador))


