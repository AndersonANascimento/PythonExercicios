# Crie um programa que leia o nome completo de uma pessoa e mostre:
#   1. O nome com todas as letras maiúsculas
#   2. O nome com todas as letras minúsculas
#   3. Quantas letras ao todo(sem considerar espaços).
#   4. Quantas letras tem o primeiro nome

nome = input('Informe o nome completo: ')
print('1. {}'.format(nome.upper()))
print('2. {}'.format(nome.lower()))
print('3. {}'.format(len(nome) - nome.count(' ')))
print('4. {}'.format(len((nome.split())[0])))
