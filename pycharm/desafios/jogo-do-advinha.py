"""import random

num = [0, 1, 2, 3, 4, 5]

escolhido = random.choice(num)"""

from random import randint # Escolhe um número entre 0 e 5

escolhido = randint(0,5)

res = int(input('Digite um número de 0 a 5: ')) # Jogador tenta adivinhar 

if res == escolhido:
    print('Você ganhou! ')
else:
    print('Você não ganhou :(')

print('O número que pensei foi {}' .format(escolhido))