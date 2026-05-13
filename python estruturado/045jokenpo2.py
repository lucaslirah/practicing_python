# Jogo do jokenpo com condições aninhadas
from random import randint
from time import sleep
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      ''')
jogador = int(input("Qual é a sua jogada? "))
# print(opcoes[computador], 'x', opcoes[jogador])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('=+'*15)
print(f'Computador jogou {opcoes[computador]}.')
print(f'Jogador jogou {opcoes[jogador]}.')
print('=+'*15)

if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
else:
    print('Jogada inválida!')
