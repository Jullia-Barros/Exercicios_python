#Tipos primitivos (int/float/bool/str(string/caractere))
#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite mais um número: '))
#soma = n1+n2
#print('A soma entre', n1 , 'e' , n2 ,'vale', soma)

#print('A soma entre {} e {} vale {}'.format(n1, n2, soma))  # {}mascara
"""
import math
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num  = int(input('Digite um número: '))
dob  = num * 2
trip = num * 3
raiz = math.sqrt(num)   #n ** (1/2) Aqui uso parenteses para forçar o programa a fazer a operação entre () primeiro.

print('Você digitou o número {}'.format(num))   #.format é um método!
print('Seu dobro é {}'.format(dob))
print('O seu triplo é {}'.format(trip))         #Para quebrar linha \n tem que estar dentro de '' <- STRING
print('E a raiz quadrada de {} é {:.2f}'.format(num,raiz))
"""
# OU pode fazer da maneira baixo:
num = int(input('Digite um número: '))
print('O dobro de {} é {}.\nO triplo é {}.\ne a raiz quadrada é {:.2f}.'.format(num, num*2, num*3, num ** (1/2)))

