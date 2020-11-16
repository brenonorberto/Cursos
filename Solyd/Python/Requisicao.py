import requests

cabecalho = {'User-agent': 'ubuntu'}
requisicao = requests.get('https://putsreq.com/qtaAsbSpsqTPo174ireR', headers = cabecalho)

print(requisicao.text)