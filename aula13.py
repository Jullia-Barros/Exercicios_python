'''for c in range(1, 11):       #No caso ele só vai escrever até o 9. Pois no python ele não considera o último elemento!
    print('Oi')

num = int(input('Digite um número: '))
for c in range(0, num+1):
    print(c)

inicio = int(input('Digite o início: '))
final = int(input('Digite o final: '))
passo = int(input('Qual será o salto: '))
for c in range(inicio, final+1, passo):
    print(c)

for c in range(1, 5+1):
    n = int(input('Digite um valor: '))
'''

soma = 0
for c in range(0, 4):
    num = int(input('Digite um valor: '))
    soma += num
print('A soma de todos os valores é {}'.format(soma))

