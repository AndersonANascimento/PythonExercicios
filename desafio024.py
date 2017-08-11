# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

NOME = 'SANTO'

cidade = input('Informe o nome da cidade: ')

check = '' if (NOME in (cidade.split())[0].upper()) else 'não'

print('O cidade {}, {} possui a palavra {}.'.format(cidade, check, NOME))
