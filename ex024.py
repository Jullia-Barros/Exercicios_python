#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTOS"

cidade = str(input('Digite a cidade em que nasceu: ')).strip()    #strip() tira os espaços
print(cidade[:5].upper() == 'SANTO')
