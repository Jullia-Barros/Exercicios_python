#Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

#na liquidação...

prec = float(input('Digite o preço do produto: '))
liqu = int(input('Informe o desconto: '))
desc = prec * 0.05                                  #5% prec * 5 / 100
novV = prec - desc
print('O valor do produto após desconto é R${:.2f}'.format(novV))