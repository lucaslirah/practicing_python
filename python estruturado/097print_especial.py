def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


mensagem = str(input('Qual a mensagem? '))
escreva(mensagem)
