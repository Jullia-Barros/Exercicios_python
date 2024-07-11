#Crie um programa que leia o nome de uma pessoa e diga se ela tem o "SILVA" no nome. Mostre true ou false

nome = str(input('Digite o seu nome completo: '))
#print('SILVA' in nome.upper())
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))     #Utilizando o operador in
