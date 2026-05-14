def ficha(n_jogador='<desconhecido>', n_cestas=0):
    print(f'O jogador {n_jogador} fez {n_cestas} cesta(s) no campeonato.')


nome_jogador = str(input('Nome do Jogador: ')).strip()
num_cestas = str(input('Número de Cestas: '))

if num_cestas.isnumeric():
    num_cestas = int(num_cestas)
else:
    num_cestas = 0
if nome_jogador == '':
    ficha(n_cestas=num_cestas)
else:
    ficha(nome_jogador, num_cestas)
