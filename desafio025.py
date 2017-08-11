# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

NOME = 'SILVA'

nome = input('Informe o nome: ')

check = '' if (NOME in nome.upper()) else 'não'

print('{}, {} possui {} no nome.'.format(nome, check, NOME))
