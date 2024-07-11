'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores ligos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
'''
num = 0
soma = 0
media = 0
opção = 0

vezes = int(input('Digite quantas vezes quer digitar os números: '))

maior = None
menor = None

contador = 0

while contador < vezes:
    num = int(input('Digite um número: '))
    soma += num

    if maior is None or num > maior:
        maior = num

    if menor is None or num < menor:
        menor = num

    continuar = input('Quer continuar a digitar os valores? (s/n):  ')
    if continuar.lower() != 's':
        break

    contador += 1

media = soma / vezes

print('A média de todos os valores digitados foi {:.1f}'.format(media))
print('O menor valor digitado foi', menor)
print('O maior valor digitado foi', maior)

