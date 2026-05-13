# Jogo do jokenpo
from random import choice
from time import sleep

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      ''')
opcao_computador = choice(opcoes)
opcao_jogador = int(input("Qual é a sua jogada? "))

if opcao_jogador == 0:
    opcao_jogador = "PEDRA"
elif opcao_jogador == 1:
    opcao_jogador = "PAPEL"
elif opcao_jogador == 2:
    opcao_jogador = "TESOURA"
else:
    print("Opção inválida, tente novamente.")
    exit()

sleep(2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print('=+'*15)
print(f'Computador jogou {opcao_computador}.')
print(f'Jogador jogou {opcao_jogador}.')
print('=+'*15)

if (opcao_jogador == 'PEDRA' and opcao_computador == 'PAPEL') or (opcao_jogador == 'PAPEL' and opcao_computador == 'TESOURA') or (opcao_jogador == 'TESOURA' and opcao_computador == 'PEDRA'):
    print('COMPUTADOR VENCEU!')
elif (opcao_jogador == 'PAPEL' and opcao_computador == 'PEDRA') or (opcao_jogador == 'PEDRA' and opcao_computador == 'TESOURA') or (opcao_jogador == 'TESOURA' and opcao_computador == 'PAPEL'):
    print('VOCÊ VENCEU!')
else:
    print('EMPATE!')
