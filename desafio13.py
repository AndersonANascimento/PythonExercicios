# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

PERC_AUMENTO = 1.15
salario = float(input('Informe o salário do funcionário: '))
print('Salário: R$ {:.2f}\nSalário(aumento 15%): R$ {:.2f}'.format(salario, salario * PERC_AUMENTO))
