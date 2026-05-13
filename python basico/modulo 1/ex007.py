aluno = input('Qual o nome do aluno? ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno {} é {:.1f}.'.format(aluno, media))
