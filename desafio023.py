# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = input('Digite um número: ')

print('*** Tratando como string ***')
print('unidade: {}'.format(num[3]))
print('dezena: {}'.format(num[2]))
print('centena: {}'.format(num[1]))
print('milhar: {}'.format(num[0]))

print('\n*** Tratando como inteiro ***')
x = int(num)    # x = 1834
m = x // 1000   # m = 1
x = x % 1000    # x = 834
c = x // 100    # c = 8
x = x % 100     # x = 34
d = x // 10     # d = 3
u = x % 10      # u = 4
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
