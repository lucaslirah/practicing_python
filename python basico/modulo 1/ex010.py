cot_dolar = 5.16
print('Cotação do dólar: {}'.format(cot_dolar))
saldo_carteira = float(input('Digite o valor do saldo de reais em carteira: '))
print('O saldo em carteira equivale a ${:.2f} dólares.'.format(saldo_carteira / cot_dolar))
