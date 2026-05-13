numero = int(input('Digite um número inteiro (até 9999): '))

if numero > 9999:
    numero = int(input('Número incorreto, digite novamente: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'A unidade do número: {unidade}')
print(f'A dezena do número: {dezena}')
print(f'A centena do número: {centena}')
print(f'O milhar do número: {milhar}')
