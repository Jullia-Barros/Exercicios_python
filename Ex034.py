#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite o seu salário bruto: '))

if salario >= 1250:
    aumento: float = salario * 0.10
    NovoSal: float = salario + aumento
    print('Seu salário com o aumento de 10% ficou de {:.2f}'.format(NovoSal))
else:
    aumento: float = salario * 0.15
    NovoSal: float = salario + aumento
    print('Seu salário com o aumento de 15% ficou de {:.2f}'.format(NovoSal))
'''
#Ou
salário = float(input('Informe o salário do funcionário: '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhaca R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))