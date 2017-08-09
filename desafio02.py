# Crie um script que leia o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

print('{}/{}/{}'.format(dia, mes, ano))
