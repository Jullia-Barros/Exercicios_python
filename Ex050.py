'''
Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i} número: '))
    if num % 2 == 0:
        soma += num
print('A soma dos números paredes digitados é', soma)







