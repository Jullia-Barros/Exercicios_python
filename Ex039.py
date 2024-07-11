'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se é a hora de se alistar.
Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
ano = date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = ano - anoNasc

if idade < 18:
    falta = 18 - idade
    print('Você ainda irá se alistar daqui a {} anos'.format(falta))
elif idade == 18:
    print('Está na hora de se alistar jovem, boa sorte')
else:
    tempo = idade - 18
    print('Já passou da hora de se alistar há {} anos'.format(tempo))
print('Você tem ou vai fazer {} anos '.format(idade))

