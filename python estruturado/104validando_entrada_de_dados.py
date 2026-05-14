def leia_int(num):
    num = input(num)
    while True:
        if num.isnumeric():
            return int(num)
        else:
            print('\033[31mValor inválido. Digite um número inteiro.\033[0m')
            num = input('Digite um número: ')


# Programa Principal
num = leia_int('Digite um número:')
print(f'Você acabou de digitar o número {num}.')
