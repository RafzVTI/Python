print('-=-' *10)
print('ESSE TRIANGULO EXISTE?')
print('-=-' *10)
c1 = float(input('Qual a medida do primeiro cateto? '))
c2 = float(input('Qual a medida do segundo cateto? '))
h = float(input('Qual a medida da hipotenusa? '))
if c1 + c2 > h:
    print('Esse triangulo existe')
else:
    print('Esse triangulo nao existe')
print('-=-' *10)
print('FIM DO PROGRAMA')
print('-=-' *10)