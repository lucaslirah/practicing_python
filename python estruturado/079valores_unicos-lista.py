lista_numeros = []
continua = 'S'

while continua != 'N':
    numero = int(input('Digite um numero: '))

    if lista_numeros.__contains__(numero):
        print('Já existe, não vou adicionar.')
    else:
        lista_numeros.append(numero)

    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continua not in 'NnSs':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()

lista_numeros.sort()

print(f'Você digitou os números: {lista_numeros}')
