aluno = {}
aluno['nome'] = str(input('Nome: '))
# nessa versão do python (3.14) já é possível utilizar aspas simples dentro de aspas simples para as keys dos dicionários
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 7 and aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
aluno['situação']

print('-=' * 30)

for key, value in aluno.items():
    print(f'- {key} é igual a {value}')
