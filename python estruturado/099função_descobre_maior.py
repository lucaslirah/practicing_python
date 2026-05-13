from time import sleep


def descobre_maior(* par):
    print('Analisando valores passados...')
    maior = 0
    par_len = len(par)
    for p in par:
        if p != 0 and p > maior:
            maior = p
        print(p, end=' ', flush=True)
        sleep(1)
    if par_len == 0:
        print(f'Nenhum valor informado.')
    elif par_len == 1:
        print(f'Apenas {par_len} valor informado.')
    else:
        print(f'Foram informados {par_len} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 30)


descobre_maior(0)
descobre_maior(0, 1, 4, 10, 7)
descobre_maior()
