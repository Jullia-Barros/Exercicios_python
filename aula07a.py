n1 = int(input('Digite um valor: ' ))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
div = n1/n2
divI = n1//n2
exp = n1**n2
print('A soma é {}, o produto vale {} e a divisão é {:.2f}'.format(s, m, div), end=' ')          #Formatando casas decimais da divisão, aceitando 2 números após a virgula!
print('Divisão inteira é {} e a potência {}'.format(divI, exp))

