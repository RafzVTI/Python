salarioa = float((input('digite o salario atual do funcionario: ')))
salariob = salarioa + (salarioa * 15 / 100)
print('O salario atual do funcionario e de R$ {} e com o aumento de 15% passara a ser de R$ {:.2f}'.format(salarioa, salariob))