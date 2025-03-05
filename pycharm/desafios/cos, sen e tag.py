import math
an = float(input('Digite o angulo que vc deseja '))
seno = math.sin(math.radians(an))
print('O SENO de {} e {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O angulo de {} tem o Tangente de {:.2f}'.format(an, tangente))