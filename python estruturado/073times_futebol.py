
times = ('Palmeiras',
         'Flamengo',
         'Fluminense',
         'São Paulo',
         'Athletico-PR',
         'Bahia',
         'Bragantino',
         'Coritiba',
         'Vitória',
         'Botafogo',
         'Atlético-MG',
         'Internacional',
         'Vasco',
         'Grêmio',
         'Cruzeiro',
         'Santos',
         'Corinthians',
         'Mirassol',
         'Remo',
         'Chapecoense')

print('~~'*20)
print(f'Lista de Times do Brasileirão: {times}.')
print('~~'*20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('~~'*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('~~'*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('~~'*20)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª posição.')
