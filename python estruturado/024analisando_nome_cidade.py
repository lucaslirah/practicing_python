nome_cidade = str(input('Diga o nome de uma cidade: ')).strip()

nome_cidade_m = nome_cidade.upper()

contem_santo = nome_cidade_m.find('SANTO')
# contem_sao = nome_cidade_m.find('SAO')

print(contem_santo)

print(
    f'O nome da cidade {'não contém'if contem_santo == -1 else 'contém'} santo.')
