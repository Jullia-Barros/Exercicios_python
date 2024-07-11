#Mostre um programa que leia um número inteiro e mostre a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))
#print(num * 1)
#print(num * 2)
#print(num * 3)
#print(num * 4)
#print(num * 5)
#print(num * 6)
#print(num * 7)
#print(num * 8)
#print(num * 9)
#print(num * 10)
'''
#ou
print('-------------------')
for count in range(10):
    print('%d X %d = %d' % (num, count+1, num*(count+1)))
print('-------------------')
'''
# ou
print('-' * 12)
print('{} X {:2} = {}'.format(num, 1, num*1))        #'{} X {:2} = {}'
print('{} X {:2} = {}'.format(num, 2, num*2))
print('{} X {:2} = {}'.format(num, 3, num*3))
print('{} X {:2} = {}'.format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print('{} X {:2} = {}'.format(num, 6, num*6))
print('{} X {:2} = {}'.format(num, 7, num*7))
print('{} X {:2} = {}'.format(num, 8, num*8))
print('{} X {:2} = {}'.format(num, 9, num*9))
print('{} X {:2} = {}'.format(num, 10, num*10))
print('-' * 12)
