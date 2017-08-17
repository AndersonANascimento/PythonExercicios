# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Informe o 1º número: '))
n2 = float(input('Informe o 2º número: '))
n3 = float(input('Informe o 3º número: '))

maior = menor = n1
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print('O menor é {:.2f}, o maior é {:.2f}.'.format(menor, maior))
