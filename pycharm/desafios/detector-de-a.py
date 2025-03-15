frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes ' .format(frase.count('a')))
print('O primeiro "A" aparece na posição {} ' .format(frase.find('a')+1))
print('O ultimo "A" aparece na posição {}' .format(frase.rfind('a')+1))