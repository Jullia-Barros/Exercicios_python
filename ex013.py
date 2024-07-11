#Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
aumento = int(input('Digite o valor do aumento: '))
calculo = salario * 15 / 100                              #Ou 0.05
NovoSal = salario + calculo
print('Após aumento de {}% o seu salario será {:.2f}'.format(aumento,NovoSal))
