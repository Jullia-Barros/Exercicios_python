#Faça um programa em que o usuário digite 2 números e o programa faça o cálculo.
num1 = int(input('\033[1;34m Digite um número: '))
num2 = int(input('\033[1;35m Digite mais um número: '))
soma:int = num1+num2
#soma = num1 + num2
print('\033[33mA soma entre {} e {} é {}!'. format(num1, num2, soma))