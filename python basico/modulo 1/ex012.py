preco_produto = float(input('Qual é o preço do produto? R$'))
# desconto = 0.2 # 20% de desconto
desconto = 5
produto_desconto = preco_produto - (preco_produto * desconto / 100)
print('O preço do produto com o desconto de {}% é de R${:.2f}.'.format(desconto, produto_desconto))
