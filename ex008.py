#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros
# Km hm dam m dm cm mm (dam = decametro, dm = decimetro)
metros = float(input('Digite o valor em mêtros: '))
centi = metros * 100
milim = metros * 1000
print('Você digitou {} mêtros'.format(metros))
print('Que tem {:.1f} centímetros'.format(centi))
print('E {} milímetros'.format(milim))

