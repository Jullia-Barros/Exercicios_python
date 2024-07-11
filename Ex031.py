#Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

#Km = int(input('Informe a distância de sua viagem em Km: '))
'''
if Km <= 200:
    passagem = Km * 0.50
    print('O valor da sua passagem é R${:.2f}'.format(passagem))
else:
    passagem = Km * 0.45
    print('O preço da sua passagem será de R${:.2f}'.format(passagem))
'''
#OU
Km = int(input('Informe a distância de sua viagem em Km: '))
passagem = Km * 0.50 if Km <= 200 else Km * 0.45                        #IF simplificado...Condição em uma linha!
print('O preço da sua passagem será de R${:.2f}'.format(passagem))
