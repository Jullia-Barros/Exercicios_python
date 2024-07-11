nome = str(input('Digite o seu nome: ')).capitalize()
if nome == 'Jullia':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Juliana' or nome == 'Gabriela' or nome == 'Giovanna':        #Estrutura condicional alinhada!
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Sara Nicolly Cynthya Jhennifer':
    print('Seu nome é forte assim como vc!')
else:
    print('Seu nome é comum!')
print('Tenha um Bom dia, {}'.format(nome))
