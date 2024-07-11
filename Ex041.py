'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER
'''

from datetime import date

AnoAtual = date.today().year
anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = AnoAtual - anoNasc
if idade <= 9:
    print('Aluno nível mirim')
elif idade <= 14:
    print('Aluno nível infantil')
elif idade <= 19:
    print('Aluno nível junior')
elif idade <= 25:
    print('Aluno nível sênior')
else:
    print('Aluno nível master')
print('O atleta tem ou fará {} anos'.format(idade))
