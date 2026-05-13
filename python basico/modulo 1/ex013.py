salário_funcionário = float(input('Qual o salário do funcionário? R$'))
porcentagem_aumento = 15
salário_com_aumento = salário_funcionário + (salário_funcionário * porcentagem_aumento / 100)

print(f'Um funcionário que recebia R${salário_funcionário:.2f}, com aumento de {porcentagem_aumento}%, passa a receber R${salário_com_aumento:.2f}')
