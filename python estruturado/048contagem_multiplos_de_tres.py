# soma múltiplos de três
soma = 0
for i in range(1, 501, 1):
    if i % 3 == 0:
        print(i)
        soma += i
print(f'A soma dos múltiplos de três entre 1 e 500 é: {soma}')
