import math
import re
import unicodedata
from pathlib import Path

import requests

LETRAS = "abcdefghijklmnopqrstuvwxyz"
ARQUIVO_CSV = Path(__file__).with_name("letter_frequency.csv")

# URLs de exemplo
URL = ["https://www.letras.mus.br/gusttavo-lima/assunto-que-doi/"]

def baixar_texto(url):
    try:
        resposta = requests.get(url, timeout=15)
        resposta.raise_for_status()
        return resposta.text
    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a URL:", erro)
        return None


def extrair_texto_principal(texto):
    bloco_musica = re.search(
        r'<div class="lyric-original">(.*?)</div>',
        texto,
        re.DOTALL
    )

    if bloco_musica:
        texto = bloco_musica.group(1)

    return texto


def limpar_texto(texto):
    # Remove tags HTML de forma simples
    texto = re.sub(r"<[^>]+>", " ", texto)

    # Deixa tudo minusculo
    texto = texto.lower()

    # Remove acentos e cedilha
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(letra for letra in texto if unicodedata.category(letra) != "Mn")

    # Mantem apenas letras de a ate z
    texto = "".join(letra for letra in texto if letra in LETRAS)

    print(f"Texto limpo: {len(texto)} caracteres")

    return texto


def calcular_frequencia(texto):
    frequencia = {}
    total = len(texto)

    if total == 0:
        return None

    for letra in LETRAS:
        frequencia[letra] = 0

    for letra in texto:
        frequencia[letra] += 1

    for letra in frequencia:
        frequencia[letra] = (frequencia[letra] / total) * 100

    return frequencia


def carregar_perfis():
    if not ARQUIVO_CSV.exists():
        print("Arquivo letter_frequency.csv nao encontrado.")
        return None

    try:
        with open(ARQUIVO_CSV, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        cabecalho = linhas[0].strip().split(";")
        nomes_idiomas = cabecalho[1:]
        perfis = {}

        for idioma in nomes_idiomas:
            perfis[idioma.lower()] = {}

        for linha in linhas[1:]:
            partes = linha.strip().split(";")
            if len(partes) < 2:
                continue

            letra = partes[0].lower()

            if letra not in LETRAS:
                continue

            for i in range(1, len(partes)):
                valor = partes[i].replace("%", "").replace("*", "").replace(",", ".")

                if valor == "":
                    numero = 0.0
                else:
                    numero = float(valor)

                idioma = nomes_idiomas[i - 1].lower()
                perfis[idioma][letra] = numero

        for idioma in perfis:
            for letra in LETRAS:
                if letra not in perfis[idioma]:
                    perfis[idioma][letra] = 0.0

        return perfis
    except Exception as erro:
        print("Erro ao ler o arquivo CSV:", erro)
        return None


def comparar_perfis(freq_texto, perfis):
    melhor_idioma = ""
    menor_distancia = None

    for idioma in perfis:
        soma = 0

        for letra in LETRAS:
            valor_texto = freq_texto.get(letra, 0)
            valor_perfil = perfis[idioma].get(letra, 0)
            soma += (valor_texto - valor_perfil) ** 2

        distancia = math.sqrt(soma)

        if menor_distancia is None or distancia < menor_distancia:
            menor_distancia = distancia
            melhor_idioma = idioma

    similaridade = 1 / (1 + menor_distancia)
    return melhor_idioma, similaridade, menor_distancia


def mostrar_top_5(frequencia):
    lista = list(frequencia.items())
    lista.sort(key=lambda item: item[1], reverse=True)
    top_5 = lista[:5]

    print("5 letras mais frequentes no texto:")
    for letra, valor in top_5:
        print(f"{letra}: {valor:.2f}%")


def analisar_url(url, perfis):
    print("=" * 60)
    print("URL analisada:")
    print(url)

    texto_bruto = baixar_texto(url)
    if texto_bruto is None:
        return

    texto_principal = extrair_texto_principal(texto_bruto)

    print()
    print("Texto antes do tratamento:")
    print(texto_principal[:1000])
    print()

    texto_limpo = limpar_texto(texto_principal)
    if texto_limpo == "":
        print("Nao foi possivel analisar o texto.")
        return

    print()
    print("Texto depois do tratamento:")
    print(texto_limpo[:1000])
    print()

    frequencia_texto = calcular_frequencia(texto_limpo)
    if frequencia_texto is None:
        print("Nao foi possivel calcular a frequencia.")
        return

    idioma, similaridade, distancia = comparar_perfis(frequencia_texto, perfis)

    print()
    print("Resultado final:")
    print(f"O texto esta em {idioma} com grau de similaridade {similaridade:.4f}")
    print(f"Distancia euclidiana: {distancia:.4f}")
    print(f"Quantidade de letras analisadas: {len(texto_limpo)}")
    print()
    mostrar_top_5(frequencia_texto)
    print()


def main():
    print("IDENTIFICADOR DE IDIOMA POR FREQUENCIA DE LETRAS")
    print()

    perfis = carregar_perfis()
    if perfis is None:
        return

    for url in URL:
        analisar_url(url, perfis)


if __name__ == "__main__":
    main()
