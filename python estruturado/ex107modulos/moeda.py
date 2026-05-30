def metade(n, m=False):
    res = n / 2
    return res if m is False else moeda(res)

def dobro(n, m=False):
    res = n * 2
    return res if m is False else moeda(res)

#aumenta n em 10%
def aumentar(n, t, m=False):    
    res = n + (n * t / 100)
    return res if m is False else moeda(res)

#diminui n em 13%
def diminuir(n, t, m=False):
    res = n - (n * t / 100)
    return res if m is False else moeda(res)

#mostrar o valor como monetário e formatado
def moeda(n):
    return f'R${n:.2f}'
