numeros = []
p_menor = []
p_maior = []
maior = menor = 0

for p in range(0, 5):
    num = int(input(f'Digite um número para a posição {p}: '))
    numeros.append(num)

    if len(numeros) == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

for p, n in enumerate(numeros):
    if n == maior:
        p_maior.append(p)
    if n == menor:
        p_menor.append(p)

print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi: {maior} na(s) posição(ões) {p_maior}.')
print(f'O menor valor digitado foi: {menor} na(s) posição(ões)  {p_menor}.')
