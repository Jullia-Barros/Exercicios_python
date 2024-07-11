somaIdade = 0
médiaIdade = 0
maioridadeHomem = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
médiaIdade = somaIdade / 4
print('A média de idade do grupo é {} anos'.format(médiaIdade))
print('O homem mais velho é o {} com {} anos de idade'.format(nomevelho, maioridadeHomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))