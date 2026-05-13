# Faça um programa quejogue par ou ímpar
# com o computador. O jogo Só será
# interrompido quando O jogador perder,
# mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint, choice

print("~"*30)
print('VAMOS JOGAR PAR OU IMPAR!')
print("~"*30)

par_impar = ("PAR", "IMPAR")
soma = vitorias = 0

while True:
    valor_jogador = int(input('Diga um valor: '))
    escolha_jogador = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]

    valor_computador = randint(0, 11)
    escolha_computador = choice(par_impar).strip()[0]

    soma = valor_jogador + valor_computador

    print(
        f'Você jogou {valor_jogador} e o computador {valor_computador}.\nTotal de {soma}.')
    print("~"*30)

    if soma % 2 == 0:
        if escolha_jogador == "P":
            print("DEU PAR, Você venceu!")
            vitorias += 1
        else:
            print("DEU PAR, Você Perdeu!")
            break
    else:
        if escolha_jogador == "I":
            print("DEU IMPAR, Você venceu!")
            vitorias += 1
        else:
            print("DEU IMPAR, Você Perdeu!")
            break

    print("Vamos Jogar novamente!")
    print("~"*30)
print(
    f'Total de vitórias: {vitorias}')
print("~"*30)
