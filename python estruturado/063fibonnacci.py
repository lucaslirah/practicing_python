# sequencia de Fibonacci
# A sequencia de Fibonacci é uma sequencia de numeros inteiros onde cada numero é a soma dos dois numeros anteriores. A sequencia começa com 0 e 1, e os numeros seguintes são calculados a partir desses dois primeiros numeros.
# Exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
numero = int(
    input('Digite um numero inteiro para calcular a sequencia de Fibonacci: '))
a = 0
b = 1
while numero > 0:
    print(a, end=' ')
    c = a
    a = b
    b += c
    numero -= 1
