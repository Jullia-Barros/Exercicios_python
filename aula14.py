'''i = 0
while i < 11:
    print(i)
    i += 1
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
print('Fim')
'''
num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
