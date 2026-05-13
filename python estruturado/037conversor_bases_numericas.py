# Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input("Digite um número inteiro: "))
print('''Escolha a base de conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"O número {numero} em binário é: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"O número {numero} em octal é: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"O número {numero} em hexadecimal é: {hex(numero)[2:].upper()}")
else:
    print("Opção inválida!")
