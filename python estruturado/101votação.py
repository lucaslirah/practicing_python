print('=' * 30)
idade = 0


def votação(ano_nascimento):
    from datetime import datetime  # escopo de importação | economiza memória
    global idade  # escopo global chamado no escopo local
    idade = datetime.now().year - ano_nascimento
    voto = ''

    if idade < 16:
        voto = 'NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        voto = 'OPCIONAL'
    else:
        voto = 'OBRIGATÓRIO'

    return voto


resultado = votação(int(input('Em que ano você nasceu? ')))

print(f'Com {idade} anos: {resultado}.')
