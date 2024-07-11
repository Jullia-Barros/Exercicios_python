'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo; OK
Qual é o nome do homem mais velho OK ;
Quantas mulheres têm menos de 20 anos.
'''
SomaIdade = 0
MediaIdade = 0
maior = 0
MaisVelho = 0
Menos_de_vinte = 0
for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p} pessoa: ')).upper()
    idade = int(input(f'Digite a idade da {p} pessoa: '))
    sexo = str(input(f'Digite o sexo [F/M] ')).lower()
    SomaIdade += idade
    MediaIdade = SomaIdade / 4

    if sexo in 'Mm' and idade > maior:
        maior = idade
        MaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        Menos_de_vinte += 1

print('A média de idades do grupo é ', MediaIdade)
print('O homem mais velho é o {} com {} anos de idade'.format(MaisVelho, maior))
print('{} mulheres tem menos de 20 anos'.format(Menos_de_vinte))



