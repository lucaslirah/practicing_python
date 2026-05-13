# Melhore o jogo do DESAFIO 028 onde o computador vai
# "pensar" em um numero de 1 a 10. So que agora o jogador
# vai tentar adivinhar ate acertar, mostrando no final quantos
# palpites foram necessários para vencer.
from random import randint
computador = randint(1, 10)

print('=+=' * 20)
print('''Sou seu computador...
      Acabei de pensar em um numero de 1 a 10.
      Voce consegue adivinhar qual foi?
      ''')
print('=+=' * 20)

acertou = False
palpites = 0

while not acertou:
    print('Vamos lá! Tente adivinhar...')
    palpite = int(input('Qual é o seu palpite? '))
    print('=+=' * 20)

    if palpite > 10 or palpite < 1:
        print('Valor inválido. Por favor, digite um numero de 1 a 10.')
    elif palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('O numero é maior do que isso.')
        else:
            print('O numero é menor do que isso.')
        print('Tente novamente.')

    palpites += 1
print(f'Parabéns! Você acertou o número {computador} em {palpites} palpites!')
