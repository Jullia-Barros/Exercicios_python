#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere o dólar 4,97

real  = float(input('Digite quantos reais você tem: '))
dolar = float(input('Digite qual o valor do dólar hoje: '))
euro = float(input('Digite qual o valor do euro hoje: '))
conv  = real * dolar
convE = real * euro
print('Você tem {:.2f} dólares\n e {} euros!'.format(conv, convE))