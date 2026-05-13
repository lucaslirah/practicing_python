def calcula_área(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}m².')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcula_área(largura, comprimento)
