# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um trângulo.
# Obs: Em todo triângulo, a medida de qualquer lado é maior que a diferença entre as medidas dos outros dois.

r1 = int(input('Informe a medida da 1ª reta: '))
r2 = int(input('Informe a medida da 2ª reta: '))
r3 = int(input('Informe a medida da 3ª reta: '))

if r1 > abs(r2 - r3) and r2 > abs(r1 - r3) and r3 > abs(r1 - r2):
    ehTriangulo = ''
else:
    ehTriangulo = 'não '

print('Os segmentos de reta de medidas {}, {} e {}, {}podem formar um triângulo.'.format(r1, r2, r3, ehTriangulo))
