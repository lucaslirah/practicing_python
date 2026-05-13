lista_numeros = []

while True:
    numero = int(input('Digite um valor: '))
    lista_numeros.append(numero)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()

    while continua not in 'SsNn':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua in 'Nn':
        break

lista_numeros.sort(reverse=True)

print('-='*30)
print(f'Você digitou {len(lista_numeros)} elementos.')
print(f'Os valores em ordem decrescente são: {lista_numeros}')
print(f'{'O valor 5 não faz parte da lista. 'if 5 not in lista_numeros else 'O valor 5 faz parte da lista.'}')
