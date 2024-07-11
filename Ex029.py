#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input('Que é velocidade atual do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[1;31mVocê foi multado no valor de R${:.2f}'.format(multa))
print('\033[1;32mBoa viagem, continue dirigindo com segurança')
