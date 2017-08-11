# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
AREA_POR_LITRO = 2.0

largura = float(input('Informe a largura(m) da parede: '))
altura = float(input('Informe a altura(m) da parede: '))
area = largura * altura
qtd_litros = area / AREA_POR_LITRO
print('Para pintar {:.2f}m² de parede são necessários {:.2f} litros de tinta.'.format(area, qtd_litros))
