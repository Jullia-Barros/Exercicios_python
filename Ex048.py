'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de 3 e que se encontram no intervalo de 1 até 500.

# último dígito do número é 0, 3, 6 ou 9.
'''
soma = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
print('A soma de todos os números primos foi', soma)

