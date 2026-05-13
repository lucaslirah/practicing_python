palavras = ('dedal',
            'bem',
            'traje',
            'terra',
            'teatro',
            'fronteira',
            'pedestal',
            'ingreme',
            'plano',
            'falar')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end='')
