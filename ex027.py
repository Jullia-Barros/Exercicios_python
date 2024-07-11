#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Por exemplo: Ana Maria de Souza
# Primeiro: Ana
# último: Souza
'''
nome_completo = str(input('Digite seu nome completo: ')).strip()        # Eliminar todos os espaços vazios

separando = nome_completo.split()

primeiro_nome = separando[0]

ultimo_nome = separando[-1] # Obtém o último nome (último elemento da lista)

print('Muito prazer em te conhecer!')
print("Seu primeiro nome é", primeiro_nome)
print("Seu último nome é", ultimo_nome)
'''
#OUTRA MANEIRA DE FAZER
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

