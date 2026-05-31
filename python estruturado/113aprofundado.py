# Capturar um número inteiro e um número real e mostrar o resultado
# Realizar validação de entrada de dados para evitar erros e travar o programa
# Entrada de dados interrompida pelo usuário (keyboard interrup)

def leia_int(num):
    while True:
        num = input(f'Digite um número Inteiro: ')
        try:
            num = int(num)
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número Inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! Entrada de dados interrompida pelo usuário.\033[0m')
            continue
        return num

def leia_float(num):
    while True:
        num = input(f'Digite um número Real: ')
        try:
            num = float(num)
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número Real válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! Entrada de dados interrompida pelo usuário.\033[0m')
            continue
        return num

# Programa Principal
num = leia_int('Digite um número inteiro:')
num1 = leia_float('Digite um número Real:')


print(f'Você acabou de digitar o número {num} e {num1}.')