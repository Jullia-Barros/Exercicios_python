'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
PALINDROMO = é quando vc consegue ler a frase de frente pra trás e de trás pra frente. EX: APOS A SOPA
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O INVERSO DE {} É {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é palíndromo')
else:
    print('A frase não é um palíndromo')




