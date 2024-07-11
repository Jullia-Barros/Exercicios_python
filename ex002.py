#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('\033[1;31mQual o seu nome? ')
#print('É um prazer te conhecer ' , nome)
print('\033[4;33mÉ um prazer te conhecer, {}!'.format(nome))