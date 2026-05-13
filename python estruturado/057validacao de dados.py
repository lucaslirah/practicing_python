# Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou'F'. Caso esteja errado, peca a digitacao
# novamente ate ter um valor correto.
sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0] #pega somente a primeira letra com fatiamento
while sexo not in 'MF':
    print('Valor inválido. Por favor, digite novamente.')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
print(f'O sexo digitado foi: {"Masculino" if sexo == "M" else "Feminino"}')
