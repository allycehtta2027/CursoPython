'''
#print('ola mundo')



comento
blocos
de codigo

# comentario de linha

nome = 'gomes'
print(nome)
peso = 80.5
altura = 1.75
instrutor = True
print(peso)
print(altura)
print(instrutor)
print(peso, type(peso))
print(instrutor, type(instrutor))


valor = 15
print(valor, type(valor))
valor = str(valor)
print(type( valor))

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

print('ola, meu nome é '+ nome + '! Tenho ' + str(idade) + ' de idade')

print('ola, meu nome é ', nome, 'Tenho ', idade, 'ano de idade!')

print(f'Ola, meu nome é {nome}, tenho {idade} de idade')


    Criar um sistema para receber o nome, idade, peso, altura
    Converter a idade para receber somente numeros inteiros
    Imprimir os tipos de dados
    Imprimir todas as informações concatenadas usando f string
'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Difite sua altura: "))

print(f'Meu nome é {nome}, \ntenho {idade} de idade, \nmeu peso é {peso}, tenho {altura} de altura')
print(type(idade))