matriz = []
lista = []
soma_pares = soma_coluna = maior_valor_linha = 0
# criar matriz 3x3
for lin in range(0, 3):
    for col in range(0, 3):
        lista.append(int(input(f'Digite um valor para [{lin}, {col}]: ')))
        if len(lista) == 3:
            matriz.append(lista[:])
            lista.clear()
print('-=' * 30)
# mostrar a matriz na tela
for lis in matriz:
    print(f'[{lis[0]:^5}] [{lis[1]:^5}] [{lis[2]:^5}]')
    # cálculo para soma de valores pares da matriz
    for i in lis:
        if i % 2 == 0:
            soma_pares += i
    # cálculo para maior valor da segunda linha da matriz
    if lis == matriz[1]:
        for i in lis:
            if i > maior_valor_linha:
                maior_valor_linha = i
    # cálculo para soma dos valores da terceira coluna da matriz
    soma_coluna += lis[2]
print('-=' * 30)
# mostrar o resultado dos cálculos
print(f'A soma dos valores pares é: {soma_pares}.')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}.')
print(f'O maior valor da segunda linha é: {maior_valor_linha}.')
