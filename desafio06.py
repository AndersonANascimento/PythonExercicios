# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, n * 2))
print('O triplo de {} vale {}.'.format(n, n * 3))
print('A raiz quadrada de {} é {:.2f}'.format(n, n ** (1 / 2)))
