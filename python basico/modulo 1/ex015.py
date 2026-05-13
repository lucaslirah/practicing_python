dias_alugados = int(input('Quantos dias alugados? '))
km_percorridos = float(input('Quantos km percorridos? '))
custo_carro = 60
custo_km = 0.15
total_pagamento = (custo_carro * dias_alugados) + (km_percorridos * custo_km)

print(f'O total a pagar é de R${total_pagamento:.2f}')
