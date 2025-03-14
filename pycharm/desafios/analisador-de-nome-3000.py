nome = str(input('Digite um nome: ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é: {}' .format(nome.upper()))
print('Seu nome em letras minusculas é: {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} ele tem {} letras' .format(separa[0], nome.find(' ')))

