#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#a soma de dois lados é sempre menor que o terceiro lado.
print('\033[1;33m-=' * 14)
print(' Analisador de triângulos')
print('-=' * 14)
Reta1 = float(input('Informe o primeiro segmento: '))
Reta2 = float(input('Informe o segundo segmento: '))
Reta3 = float(input('Informe o terceiro segmento: '))

if (Reta1 + Reta2) > Reta3 and (Reta2 + Reta3) > Reta1 and (Reta3 + Reta1) > Reta2:
    print('\033[1;32mOs segmentos acima formam um triângulo')
else:
    print('\033[1;31mOs segmentos acima não formam um triângulo')

