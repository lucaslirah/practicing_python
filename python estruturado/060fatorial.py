# programa paa calcular o fatorial de um numero inteiro
# O fatorial de um numero inteiro n é o produto de todos os numeros inteiros positivos menores ou iguais a n.
# O fatorial de 0 é definido como 1.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# existe no python o método fatorial() na lib math

numero = int(input('Digite um numero inteiro para calcular o fatorial: '))
fatorial = 1

print(f'{numero}! = ', end='')

# while numero > 0:
#     print(f'{numero}', end='')
#     print(' x ' if numero > 1 else ' = ', end='')
#     fatorial *= numero
#     numero -= 1

# print(f'{fatorial}.')

for i in range(numero, 0, -1):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial *= i

print(f'{fatorial}.')
