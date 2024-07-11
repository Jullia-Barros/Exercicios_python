'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
anoAtual = date.today().year
idade = 0
maiorIdade = 0
menorIdade = 0
for p in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {p} pessoa: '))
    idade = anoAtual - nasc
    if idade >= 18:
        maiorIdade = maiorIdade + 1
    else:
        menorIdade = menorIdade + 1

print('{} pessoas já são maiores de idade'.format(maiorIdade))
print('{} pessoas já são menores de idade'.format(menorIdade))
