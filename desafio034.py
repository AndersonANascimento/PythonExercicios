# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

AUMENTO_10PERC = 1.1
AUMENTO_15PERC = 1.15

salario = float(input('Informe o salário: '))

if salario > 1250.000:
    aumento = salario * AUMENTO_10PERC
else:
    aumento = salario * AUMENTO_15PERC

print('Seu salário de R$ {:.2f} sofrerá um aumento, passando para R$ {:.2f}.'.format(salario, aumento))
