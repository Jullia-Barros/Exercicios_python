#Faça um programa para sotear um dos quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
nome = [nome1, nome2, nome3, nome4]
sorteio = choice(nome)
print('O aluno escolhido foi {}'.format(sorteio))


