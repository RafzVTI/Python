import math
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
hi = math.hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))