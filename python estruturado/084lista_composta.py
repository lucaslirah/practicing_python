pessoas = []
pessoa = []
maior_peso = menor_peso = 0
pessoas_maior_peso = []
pessoas_menor_peso = []

while True:
    pessoa.append(str(input('Nome: ')).title().strip())
    pessoa.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('Continuar? [S/N] ')).upper().strip()

    if continuar in 'Nn':
        break

for p in pessoas:
    if p[1] == maior_peso:
        pessoas_maior_peso.append(p[0])
    if p[1] == menor_peso:
        pessoas_menor_peso.append(p[0])

print(
    f'Ao todo, você cadastrou {len(pessoas)} {'pessoa' if len(pessoas) == 1 else 'pessoas'}.')
print(f'O maior peso é {maior_peso}. Peso de {pessoas_maior_peso}.')
print(f'O menor peso é {menor_peso}. Peso de {pessoas_menor_peso}.')
