'''
Refaça o desafio 009, mostrando  a tabuada de um número que o usuário escolher,
só que agora utiizando um laço for
'''
num = int(input('Qual tabuada você quer? '))
for i in range(10):
   print('%d X %d = %d' % (num, i+1, num*(i+1)))


