'''
nome = str(input('Qual o seu nome: '))
if nome == 'Jullia':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))
'''
#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#media = (n1+n2) / 2
#if media >= 6:
    #print('Sua média foi {:.1f}, Parabéns!'.format(media))
#else:
    #print('Sua média foi {:.1f}, está abaixo do esperado!'.format(media))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2) / 2
print('A sua média foi {}'.format(media))
print('PARABÉNS' if media >= 6 else 'ESTUDE MAIS!')
