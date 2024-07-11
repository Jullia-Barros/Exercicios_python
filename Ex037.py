'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
opcao = int(input('Como irá converter esse número?. Sendo:\n1-Converter para Binário\n2-Converter para Octal\n3-Converter para Hexadecimal\nDigite aqui: '))
if opcao == 1:
    print('O número em binário é {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número em octal é {}'.format(num, oct(num)))
elif opcao == 3:
    print('O número em hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opção inválida. Por favor, digite 1,2, ou 3')


