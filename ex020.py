#O mesmo professor do desafio anterior quer sotear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random

nome1 = (input('Digite o nome do aluno 1: '))
nome2 = (input('Digite o nome do aluno 2: '))
nome3 = (input('Digite o nome do aluno 3: '))
nome4 = (input('Digite o nome do aluno 4: '))
nomes = [nome1, nome2, nome3, nome4]
ordem = random.shuffle(nomes) #shuffle para embaralhar
#print('A apresentação começara com {}'.format(ordem))
print("Ordem para apresentação:")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
'''
#2 forma de se fazer:
from random import shuffle
n1 = str(input('Digite o primeiro aluno: '))
n2 = str(input('Digite o segundo aluno: '))
n3 = str(input('Digite o terceiro aluno: '))
n4 = str(input('Digite o quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem da apresentação será ')
print(lista)

