# nome = input('Digite seu nome: ')
# print('Bem vindo ao Python, {0:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {0},\no produto é {1} e a\ndivisão é {2:.3f}.'.format(s, m, d), end=' ')
print('Divisão inteira {0} e potência {1}'.format(di, e))
