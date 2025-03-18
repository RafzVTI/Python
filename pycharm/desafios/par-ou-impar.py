print('-=-' *10)
print('Detector de par ou ímpar')
print('-=-' *10)

num = float(input('Digite um número: '))
if num % 2 == 0:
    print('O numero {} é Par' .format(num))
else:
    print('O numero {} é Ímpar' .format(num))