'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: Todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: Todos so lados diferentes
'''

seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))

if (seg1 + seg2) > seg3 and (seg2 + seg3) > seg1 and (seg1 + seg3) > seg2:
    if seg1 == seg2 and seg1 == seg3:                                       #Ou seg1 == seg2 == seg3
        print('De acordo com os segmentos, o triângulo é equilátero')
    elif seg1 == seg2 or seg1 == seg3 or seg3 == seg2:
        print('De acordo com os segmentos, o triângulo é isósceles')
    elif seg1 != seg2 and seg2 != seg3:                                     #Aqui eu poderia colocar só else:
        print('De acordo com os segmentos, o triângulo é escaleno')
else:
    print('\033[1;31mOs segmentos acima não formam um triângulo')

#Condição alinhada é quando tem um if dentro de outro if

