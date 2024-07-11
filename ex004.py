#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre eles.
# INT / FLOAT / BOOL / STR / isnumeric / isalpha

msg = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(msg))

#msg = int(input('Digite algo: '))
#print(msg)

#boleano = bool(input('Digite algo: '))
#print(msg)

#msg = input('Digite um valor: ')
#print(msg.isalpha()) # Verfica se o valor digitado é letra e retorna.

#msg = input('Digite um valor: ')
print('É númerico: ', msg.isalnum())            # Verfica se o valor digitado é letra ou número e retorna.

print('É alfabético: ', msg.isalpha())

#msg = input('Digite um valor: ')
print('É alfanumerico: ', msg.isnumeric())       # Verfica se o valor digitado é número e retorna.

print('Está em maiusculas: ', msg.isupper())

print('Esta em minuculas: ', msg.islower())