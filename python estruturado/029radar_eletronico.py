# radar eletronico que calcula a velocidade do carro e o multa se exceder 80km/h, com 7,00 a cada km ultrapassado
velocidade_atual = int(input("Qual é a velocidade atual do carro?"))

if velocidade_atual > 80:
    multa = float((velocidade_atual - 80) * 7)
    print(
        f"Você está a {velocidade_atual}km/h, acima do limite de 80km.\nMultado em R${multa:.2f}!")

print("Tenha um bom dia! Dirija com segurança!")
