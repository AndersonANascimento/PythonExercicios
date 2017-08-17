# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
import random

n = random.randint(1, 5)
num = input('Descubra o número de 0 a 5 escolhido pelo computador: ')
# print('{} = {}'.format(n, num))
print('Você venceu!' if(n == int(num)) else 'Você perdeu!')
