from random import randint
from time import sleep
numeros = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numero = randint(1, 10)
        numeros.append(numero)
        print(numero, end=' ', flush=True)
        sleep(0.4)
    print('PRONTO!')


def soma_par():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


sorteia()
soma_par()
