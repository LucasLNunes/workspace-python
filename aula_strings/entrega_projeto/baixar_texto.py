import requests


def baixar_texto(url):
    try:
        resposta = requests.get(url, timeout=15)
        resposta.raise_for_status()
        return resposta.text
    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a URL:", erro)
        return None
