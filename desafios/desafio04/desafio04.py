#Esse programa mostra todas as informações de um valor digitado
#This program show all the information about a value Typed
n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(n))
print('A string digitada é um número?')
print(n.isnumeric())
print('A string digitada é uma letra?')
print(n.isalpha())
print('A string digitada está em caixa baixa?')
print(n.islower())
print('A string digitada está em caixas altas?')
print(n.isupper())
print('A string digitada é um espaço?')
print(n.isspace()) 
