# Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto.

preco = float(input('Informe o preço do produto: '))
print('Preço: {:.2f}\nPreço(desconto 5%): {:.2f}'.format(preco, preco * 0.95))
