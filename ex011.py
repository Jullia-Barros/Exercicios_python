#Faça um programa que leia a altura e largura de uma parede em mêtros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m.

altura  = float(input('Digite a altura da parede em mêtros: '))
largura = float(input('Digite a largura da parede em mêtros: '))
areaPar = altura * largura
#tinta   = 2 * areaPar
quant_tinta = areaPar / 2
print('A área da parede é: {}m²'.format(areaPar))
print('E será necessário {:.1f}l de tinta para pintar a parede!'.format(quant_tinta))
'''
# Posso também fazer da maneira abaixo:

def calcular_area_parede(altura, largura):
    return altura * largura

def calcular_quantidade_tinta(area):
    return area / 2  # Cada litro de tinta pinta uma área de 2m²

def main():
    # Solicitar a altura e largura da parede ao usuário
    altura = float(input("Digite a altura da parede em metros: "))
    largura = float(input("Digite a largura da parede em metros: "))

    # Calcular a área da parede
    area_parede = calcular_area_parede(altura, largura)

    # Calcular a quantidade de tinta necessária
    quantidade_tinta = calcular_quantidade_tinta(area_parede)

    # Exibir os resultados
    print(f"A área da parede é: {area_parede} metros quadrados")
    print(f"A quantidade de tinta necessária é: {quantidade_tinta} litros")

if __name__ == "__main__":
    main()
'''