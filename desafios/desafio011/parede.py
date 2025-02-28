altura = int(input('Digite a altura da parede em metros: '))
largura = int(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2 
print('Para a area de sua parede, que corresponde a {}m², voce precisara de {} litros de tinta para pinta-la.'.format(area, tinta))