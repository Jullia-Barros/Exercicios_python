num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opção = int(input('''Digite uma opção: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números 
[5] Sair do programa 
Digite aqui: '''))
maior = 0
while opção < 4:
    if opção == 1:
        soma = num1 + num2
        print('A soma dos dois valores digitados é', soma)
    if opção == 2:
        multiplicando = num1 * num2
        print('A multiplicação dos dois valores digitados é', multiplicando)
    if opção == 3:
        if num1 > num2:
            maior = num1
        if num2 > num1:
            maior = num2
        print('O maior valor digitado foi o', maior)
    if opção == 4:
        novoNum1 = int(input('Digite um novo valor: '))
        novoNum2 = int(input('Digite outro valor: '))
        num1 = novoNum1
        num2 = novoNum2
        print('Novos valores {} e {} alterados com sucesso'.format(num1, num2))
        # opção = int(input('Digite uma opção: '))  # volte para o menu principal...pensar em algo
    if opção == 5:
        print('Você saiu do programa')
    if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
        print('Opção Inválida. Tente novamente!')
    opção = int(input('''Digite uma opção: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números 
[5] Sair do programa 
Digite aqui: '''))
