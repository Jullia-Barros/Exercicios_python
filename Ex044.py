'''
Calcule o valor a ser pago por um produto, considerando o seu preço normal e forma de pagamento:
Á vista dinheiro/cheque: 10% de desconto.
Á vista no cartão: 5% de desconto
Em até 2X no cartão: preço normal
3X ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' AMERICANAS '))                 #Esse simbolo está sendo usada para centralizar o meu titulo do programa.^
VlrProd = float(input('Digite o valor do produto: '))
FormPag = int(input('Escolha a forma de pagamento, sendo: \n1-Dinheiro/Cheque\n2-Á vista no cartão\n3-Até 2X no cartão\n4-3X ou mais no cartão\nDigite aqui: '))
desconto = 0
NovoValor = 0
juros = 0
if FormPag == 1:
    desconto = VlrProd * 0.10                       #desconto = (VlrProd * 10 / 100)
    NovoValor = VlrProd - desconto
    print('Após o desconto de 10% o produto vai sair R${:.2f}'.format(NovoValor))
elif FormPag == 2:
    desconto = VlrProd * 0.05
    NovoValor = VlrProd - desconto
    print('Após o desconto de 5% o produto vai sair R${:.2f}'.format(NovoValor))
elif FormPag == 3:
    NovoValor = VlrProd / 2
    print('Sua compra será parcelada em 2x de R${:.2f} '.format(NovoValor))
elif FormPag == 4:
    juros = VlrProd * 0.20
    NovoValor = VlrProd + juros
    parcelas = int(input('Quantas parcelas: '))
    CalcParcelas = NovoValor / parcelas
    print('Sua compra será parcelada em {}X de R${:.2f} com juros\nSua compra de R${:.2f} vai custar R${:.2f}'.format(parcelas, CalcParcelas, VlrProd, NovoValor))
else:
    print('\033[1;31mOpção inválida. Por favor, digite novamente')
