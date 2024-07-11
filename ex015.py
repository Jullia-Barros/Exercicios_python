#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias  = int(input('Digite quantos dias está com o veículo: '))
km    = float(input('Digite quantos KM percorreu: '))
pagar = km * 0.15 + dias * 60
print('O total a pagar é R${:.2f}.'.format(pagar))