nome_completo = str(input("Digite o seu nome completo: "))

nome_maiusuculas = nome_completo.strip().upper()
nome_minusculas = nome_maiusuculas.lower()

nome_separado = nome_completo.split()
primeiro_nome = nome_separado[0]
letras_no_primeiro_nome = len(primeiro_nome)

nome_sem_espaço = ''.join(nome_separado)
letras_no_nome = len(nome_sem_espaço)

print(f'Seu nome é {nome_completo}')
print(f'Em maiúsculas: {nome_maiusuculas}. Em minúsculas: {nome_minusculas}')
print(f'Seu nome tem ao todo {letras_no_nome} letras.')
print(
    f'Seu primeiro nome é {primeiro_nome} e tem {letras_no_primeiro_nome} letras.')

#nome = str(input("Digite seu nome completo: ")).strip()
#print(f'Nome em maiúsculas: {nome.upper()}')
#print(f'Nome em minúsculas: {nome.lower()}')
#print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
#print(f'Seu primeiro nome tem ao todo {nome.find(' ')} letras.')