'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''

VlrCasa = float(input('Qual o valor da casa? R$ '))
Salario = float(input('Qual o seu salário? R$ '))
AnosPag = int(input('Quantos anos de financiamento? '))

#Cálculo da prestação mensal

PrestMensal = VlrCasa / (AnosPag * 12)

# Verifica se a prestação mensal excede 30% do salário
limite_prestacao = Salario * 0.3            #Salário * 30 / 100

if PrestMensal <= limite_prestacao:
    print('Empréstimo aprovado')
    print('O valor da prestação mensal será de R${:.2f}'.format(PrestMensal))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(VlrCasa, AnosPag, PrestMensal))
    print('Empréstimo negado! A prestação mensal excede 30% do salário.')


