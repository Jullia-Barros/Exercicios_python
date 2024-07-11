#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#ano é divisível por 4, com exceção dos anos que são divisíveis por 100, a menos que também sejam divisíveis por 400.

from datetime import date

print('Nesse programa será verificado se o ano que digitou e bissexto ou não!')
ano = int(input('Digite o ano que quer analisar? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):           #Se o ano é divisil por 4....
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
