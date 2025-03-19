print('-=-' *10)
print('Custo de viagem'.upper())
print('-=-' *10)
km = float(input('Qual é a distância da viagem? '))
if km <= 200:
    pagar = km * 0.50
    print('O valor da viagem será de R${}, pois você viajará {} KM' .format(pagar, km))
else:
    pagar = km * 0.45
    print('O valor da viagem será de R${}, pois você viajará {} KM'.format(pagar, km))

print('-=-' *10)