# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores.
soma = media = maior = menor = contador = 0
continuar = "S"
# numeros = []

while continuar == "S":
    numero = int(input("Digite um número para ser somado: "))
    soma += numero
    contador += 1
    # numeros.append(numero)
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    else:
        menor = numero

    continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]

    if continuar not in "SN":
        while continuar not in "SN":
            print("Digite uma resposta válida! S ou N")
            continuar = str(
                input("Deseja continuar [S/N]? ")).upper().strip()[0]

media = soma / contador
# maior = max(numeros)
# menor = min(numeros)

print(f'''
    Saiu do programa!
    Soma: {soma}, média: {media:.2f}, maior valor: {maior}, menor valor: {menor}
    ''')
