#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
#basta multiplicar a temperatura em graus Celsius por 1,8 e somar 32.
graus  = float(input('Digite a temperatura do dia: '))
calcul = (graus * 1.8) + 32
print('Você digitou {}ºC e a temperatura em Fahrenheit é {}ºF.'.format(graus, calcul))


