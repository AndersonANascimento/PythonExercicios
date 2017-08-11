# Faça um programa que leia uma frase pelo teclado e mostre:
#   1. Quantas vezes aparece a letra "A"
#   2. Em que posição ela aparece a 1ª vez
#   3. Em que posição ela aparece a última vez

LETRA = 'A'

frase = input('Digite uma frase: ')

print('1. A letra "{}" aparece {} vezes.'.format(LETRA, frase.upper().count(LETRA)))
print('2. Ela aparece a 1ª vez na posição {}.'.format(frase.upper().find(LETRA)))
print('3. Ela aparece a última vez na posição {}.'.format(frase.upper().rfind(LETRA)))
