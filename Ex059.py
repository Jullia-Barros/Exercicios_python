'''
Crie um programa que leia 2 valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números   #Digitar novamente outros numeros
[5] sair do programa
seu programa deverá realizar a operação solicitada em cada caso.
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opção = int(input('''Digite uma opção: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números 
[5] Sair so programa 
Digite aqui: '''))
maior = 0
while opção < 4:
if opção == 1:
    soma = num1 + num2
    print('A soma dos dois valores digitados é', soma)
elif opção == 2:
    multiplicando = num1 * num2
    print('A multiplicação dos dois valores digitados é', multiplicando)
elif opção == 3:
    if num1 > num2:
        maior = num1
    if num2 > num1:
        maior = num2
    print('O maior valor digitado foi o', maior)
elif opção == 4:
    novoNum1 = int(input('Digite um novo valor: '))
    novoNum2 = int(input('Digite outro valor: '))
    num1 = novoNum1
    num2 = novoNum2
    print('Novos valores {} e {} alterados com sucesso'.format(num1, num2))
    #opção = int(input('Digite uma opção: '))        #volte para o menu principal...pensar em algo
elif opção == 5:
    print('Você saiu do programa')
elif opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
    print('Opção Invalida. Tente novamente!')

    opção = int(input('''Digite uma opção:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Digite aqui: 
'''))

