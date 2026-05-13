# aprovando emprestimo
# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação
# mensal não pode exceder 30% do salário ou então o
# empréstimo será negado
salario = float(input("Qual é o salário do comprador? R$"))
valor_casa = float(input("Qual é o valor da casa? R$"))
anos = int(input("Em quantos anos ele vai pagar? "))
prestacao_mensal = valor_casa / (anos * 12)
if prestacao_mensal > (salario * 0.3):
    print(
        f"Empréstimo negado! A prestação mensal de R${prestacao_mensal:.2f} excede 30% do salário.")
else:
    print(
        f"Empréstimo aprovado! A prestação mensal de R${prestacao_mensal:.2f} está dentro do limite permitido.")
