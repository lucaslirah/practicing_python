# TESTE LISTA PYTHON
# carro = []
# carros = []

# print('-='*5, 'CADASTRO DE CARROS', '-='*5)
# for c in range(0, 2):
#     marca_carro = str(input('Marca: ')).strip().title()
#     ano_carro = int(input('Ano: '))
#     modelo_carro = str(input('Modelo: ')).strip().title()

#     carro.append(marca_carro)
#     carro.append(ano_carro)
#     carro.append(modelo_carro)

#     carros.append(carro[:])
#     carro.clear()
#     print('-='*20)

# print(carros)

# TESTE DICIONÁRIOS PYTHON
""" carros = []
carro = {}

print('-='*5, 'CADASTRO DE CARROS', '-='*5)
for car in range(0, 2):
    carro['marca'] = str(input('Marca: ')).strip().title()
    carro['modelo'] = str(input('Modelo: ')).strip().title()
    carro['ano'] = int(input('Ano: '))
    carros.append(carro.copy())
    print('-=' * 20)
for car in carros:
    car['tipo'] = str(
        input(f'Digite um tipo para o carro {car['marca'], car['modelo']}: '))
    print('-=' * 20)
    for key, value in car.items():
        print(f'{key.title()} é {value}.')
print('-=' * 20)

print(carros) """