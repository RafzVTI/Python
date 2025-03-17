n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Parabens, voce foi aprovado!')
else:
    if m > 6:
        print('Voce foi muito bem, parabens!')
    else:
        print('Reprovado!')


print('Sua media e {}' .format(m))
