#Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome  = input('Digite o nome do aluno(a): ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2) / 2
print('{} ficou com {:.1f} na média!'.format(nome,media))
