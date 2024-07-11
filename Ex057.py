'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''
opcao = 'F'
while opcao == 'F' or 'M':
    sexo = str(input('Digite o seu sexo: ')).upper()
    if sexo != 'F' or sexo != 'M':
        print('Opção Inválida, digite F para feminino ou M para masculino')
print('Obrigada pela participação')




#FAZERRRRRRRRRRRR