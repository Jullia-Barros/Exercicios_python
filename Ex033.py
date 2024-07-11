#Faça um programa que leia três números e mostre qual é o maior e o menor.
'''
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

numeros = [num1, num2, num3]       #Divide os números inseridos em uma lista de strings

maior = max(numeros)                            #Utilizando as funções max
menor = min(numeros)                            #Utilizando as funções min

print('O maior número é', maior)
print('O menor número é', menor)
'''
#OU
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
menor = num1
maior = num2

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor valor digitado foi {}'.format(menor))

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior valor digitado foi {}'.format(maior))
