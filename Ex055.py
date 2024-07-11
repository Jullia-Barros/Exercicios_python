'''
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p} pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso diditado foi {}'.format(maior))
print('O menor peso digitado foi {}'.format(menor))

