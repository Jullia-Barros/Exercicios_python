#frase = 'Curso em Vídeo Python'
#print(frase)

#Utilizando a técnica de fatiamento.
#frase = 'Curso em Vídeo Python'
'''
print(frase[3])            #É a 4 letra.
print(frase[3:13])         #Indica o inicio e fim da string que vc deseja.
print(frase[:13])          #Do ínico até o índice 13 da minha string.
print(frase[13:])          #Do índice 13 até o final.
print(frase[0:15:2])        #Vai começar com a letra C até o indice 15 pulando de 2 em 2.
print(frase[::2])           #Não sei o ínicio e nem o final, mas quero pulando de 2 em 2.
print(frase[1::2])          #Sei o ínicio, mas não sei o final. O Python vai contar de 2 em 2 até o final da string.
'''
#print("""Aqui eu posso escrever um texto sem precisar usar vários prints ou ficar
#pulando linha""")

#A VARIÁVEL FRASE É UMA CADEIA DE CARACTERES.
#NO PYTHON TUDO É OBJETO. OU SEJA, VC CONSEGUE COLOCAR . E UM MÉTODO DEPOIS DA SUA VARIÁVEL.
frase = 'Curso em Vídeo Python'
#print(frase.count('o'))             #Quantas vezes tem o 'o' na minha frase.

#print(frase.upper().count('O'))     #Pega a frase, joga para maiusculo e conta quantos 'O' maisculo terá na frase.

#print(len(frase))

#print(len(frase.strip()))           #strip vai remover os espaços vazios.

#print(frase.replace('Vídeo', 'Automação'))

#print('Curso' in frase)         #tem a palavra Curso na frase... Retorna .T. ou .F.
#print(frase.find('Vídeo'))      #Qual posição começa uma palavra.

#print(frase.lower().find('vídeo'))
#print(frase.split())

dividido = frase.split()
print(dividido[3]) #print(dividido[3] [2]) Aqui está falando que ele vai pegar a 3 string e a 2 palavra.
