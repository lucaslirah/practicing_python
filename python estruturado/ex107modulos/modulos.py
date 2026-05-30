import moeda

preco = float(input('Digite um valor: '))

print(f'O preço {moeda.moeda(preco)} aumentado em 10% é {moeda.aumentar(preco, 10, True)}')
print(f'O preço {moeda.moeda(preco)} diminuído em 13% é {moeda.diminuir(preco, 13, True )}')
print(f'O preço {moeda.moeda(preco)} dividido por 2 é {moeda.metade(preco, True )}')
print(f'O preço {moeda.moeda(preco)} multiplicado por 2 é {moeda.dobro(preco, True)}')
