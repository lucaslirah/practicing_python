# Verificar se o site pudim está online ou não e tratar possíveis erros de conexão

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br', timeout=3)
except Exception as e:
    print(f'ERRO: {e}')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Site Pudim acessível com sucesso.')
    site.read()
    print(site.read())
