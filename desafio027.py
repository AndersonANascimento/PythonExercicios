# Faça um program que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Informe o nome: ')

parts = nome.split()

print('First Name: {}'.format(parts[0]))
print('Last  Name: {}'.format(parts[len(parts) - 1]))
