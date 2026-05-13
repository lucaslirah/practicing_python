from datetime import datetime
ano_atual = datetime.now().year
trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = ano_atual - int(input('Ano de Nascimento: '))
trabalhador['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
while True:
    if trabalhador['sexo'] not in 'MmFf':
        trabalhador['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    else:
        break
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não possui): '))
if trabalhador['ctps'] == 0:
    print('-=' * 30)
else:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    ano_contribuição = ano_atual - trabalhador['contratação']

    if trabalhador['sexo'] in 'Mm':
        trabalhador['aposentadoria'] = trabalhador['idade'] + \
            (35 - ano_contribuição)
    else:
        trabalhador['aposentadoria'] = trabalhador['idade'] + \
            (30 - ano_contribuição)
for key, val in trabalhador.items():
    print(f'  - {key}: {val}')
