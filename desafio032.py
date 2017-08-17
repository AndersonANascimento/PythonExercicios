# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Informe um ano qualquer: '))

if ano % 400 == 0:
    print("Ano Bissexto")
elif ano % 4 == 0:
    if ano % 100 != 0:
        print("Ano Bissexto")
    else:
        print("Não é um ano Bissexto")
else:
    print("Não é um ano Bissexto")
