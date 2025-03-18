print('-=-' *10)
print('DETRAN!')
print('-=-' *10)

velo = float(input('Qual foi a velociadade que o carro passou pelo radar? '))

if velo > 80:
    dif = velo - 80
    print('Multado! A multa que deverá ser paga é de de R${}' .format(dif * 7))
else:
    print('Velocidade normal, tudo certo! Dirija com segurança!')