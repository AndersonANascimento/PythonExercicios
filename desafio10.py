# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar.

real = float(input('Informe R$: '))
dolar = real / 3.27
print('Você possui US$ {:.2f}'.format(dolar))