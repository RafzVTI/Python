dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))
pagar = (dias*60) + (km*0.15)
print('O total a pagar e de R${:.2f}'.format(pagar))