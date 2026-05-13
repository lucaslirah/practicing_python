from random import randint
from time import sleep
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print('Valores sorteados:')
for key, val in jogadores.items():
    print(f'{key} tirou {val} no dado.')
    sleep(1)
print('-=' * 30)
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print(f' == RANKING DOS JOGADORES ==')
for rank, jogador in enumerate(ranking):
    sleep(1)
    print(f'  {rank+1}º lugar: {jogador[0]} com {jogador[1]}')
