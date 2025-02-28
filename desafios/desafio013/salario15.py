salarioa = (input('digite o salario atual do funcionario: '))
salarioa = int(salarioa)
salariob = salarioa + (salarioa * 15 / 100)
print('O salario atual do funcionario e de R$ {} e com o aumento de 15% passara a ser de R$ {}'.format(salarioa, salariob))