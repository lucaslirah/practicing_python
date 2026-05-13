valor_em_metros = float(input('Digite o valor em metros a ser convertido: '))
valor_em_centimetros = valor_em_metros * 100
valor_em_milimetros = valor_em_metros * 1000
valor_em_quilometros = valor_em_metros / 10000

print('{}m equivale a {:.2f}cm, {:.2f}mm e {:.8f}km'.format(valor_em_metros,
      valor_em_centimetros, valor_em_milimetros, valor_em_quilometros))
