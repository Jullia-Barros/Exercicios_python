'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
Média abaixo de 5.0: Reprovado
Média entre 5.0 e 6.9: Recuperação
Média 7.0 ou superior: Aprovado
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Aluno está reprovado')
elif 7 > media >= 5:
    print('Aluno está em recuperação')
else:
    print('Aluno está aprovado')
print('Sua média é {:.1f}'.format(media))

