from time import sleep


def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}.')
    sleep(3)
    if fim == 0:
        fim -= 1
        pas = int(-pas)
    else:
        fim += 1
    for c in range(ini, fim, pas):
        print(f'{c}', end=' ', flush=True)  # para novas versões
        sleep(0.5)
    print('FIM!', end='', flush=True)
    print()
    print('-=' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 30)
contador(inicio, fim, passo)
