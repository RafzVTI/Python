print('-=-' *10)
print('AUMENTO SALARIAL')
print('-=-' *10)
salario = float(input('Qual o sálario do funcionario? '))
if salario > 1250.00:
    salarioa = salario + (salario / 10)
if salario <= 1250.00:
    salarioa = salario + (salario * 15 / 100)

print('O salario desse funcionario passara de R${:.2f} para R${:.2f}' .format(salario, salarioa))

print('-=-' *10)
print('FIM DO PROGRAMA')
print('-=-' *10)