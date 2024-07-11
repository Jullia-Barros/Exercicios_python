print('\033[1;37m Olá, Mundo!\033[m')                #1-Estilo/2-Text/3-Fundo
print('\033[1;34m Estou aprendendo a colocar cores no terminal!')
print('\033[7;37m Invertendo o Fundo!\033[m')

a = 3
b = 5
print('Os valores são \033[34m{} e \033[33m{}'.format(a, b))

print('Os valores são \033[34m{}\033[m e \033[33m{}\033[m'.format(a, b))          # \033[m Para a formatação não atingir a letra e

#OUTRA FORMA DE USAR AS CORES COM FORMAT!

nome = 'Jullia'
print('Muito prazer em te conhecer, {}{}{}!'.format('\033[1;34m', nome, '\033[m'))      #{} chave