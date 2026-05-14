def calcula_fatorial(num, show=False):
    """
    calcula_fatorial(num, show=False)
    ->Faz o cálculo do fatorial de um número

    Args:
        num (int): O número a ser calculado
        show (bool, optional): Mostrar ou não a conta. Defaults to False.

    Returns:
        return: O valor do Fatorial de um número num.
    """
    fatorial = 1
    print('=' * 30)
    for i in range(num, 0, -1):
        if show:
            print(f'{i}', end='')
            print(' x ' if i > 1 else ' = ', end='')
        fatorial *= i
    return fatorial


print(calcula_fatorial(6, True))
help(calcula_fatorial)