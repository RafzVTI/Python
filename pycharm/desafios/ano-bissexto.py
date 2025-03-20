from datetime import date
print('-=-' *10)
print('-ANO BISSEXTO-')
print('-=-' *10)
ano = int(input('Qual ano deseja verificar? Se quiser saber do ano atual digite "0" ')) #recebe o ano que o usuario quer saber
if ano == 0:
    ano = date.today().year #pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto' .format(ano)) #retorna que é bissexto
else:
    print('O ano de {} não é bissexto' .format(ano)) #retorna que não é bissexto
print('-=-' *10)
print('FIM DO PROGRAMA')
print('-=-' *10)