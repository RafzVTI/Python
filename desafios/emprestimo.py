print('='*20)
print('EMPRÉSTIMO')
print('='*20)
casa = float(input('Qual o valor da casa em R$: '))
tempo = int(input('Quantos anos de financiamento? '))
salario = float(input('Qual o seu sálario '))
prestação = casa / (tempo * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${} a prestacao sera de {:.2f}'.format(casa, prestação))
if prestação <= minimo:
    print('Emprestimo aprovado')
else:
    print('Negado! ')