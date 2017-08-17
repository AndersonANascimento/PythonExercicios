# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
# para viagens de até 200Km e R$ 0,45 para viagens mais longas

d = float(input('Informe a distância(km) da viagem: '))

if d > 200:
    preco = d * 0.45
else:
    preco = d * 0.5

print('O preço da passagem é R$ {}.'.format(preco))
