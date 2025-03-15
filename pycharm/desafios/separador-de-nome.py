nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(n)
print('Seu nome é {} e seu primeiro nome é {} e o último é {}' .format(nome, n[0], n[len(n)-1]))
