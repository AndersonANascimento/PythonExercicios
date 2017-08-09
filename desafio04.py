# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele

obj = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(obj)))
print('Só tem espaços?', obj.isspace())
print('É um número?', obj.isnumeric())
print('É alfabético?', obj.isalpha())
print('É alfanumérico?', obj.isalnum())
print('Está em maiúsculo?', obj.isupper())
print('Está em minúsculo?', obj.islower())
print('Está em capitalizado?', obj.istitle())
