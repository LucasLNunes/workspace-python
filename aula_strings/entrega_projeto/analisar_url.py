from baixar_texto import baixar_texto
from calcular_frequencia import calcular_frequencia
from comparar_perfils import comparar_perfis
from extrair_texto_principal import extrair_texto_principal
from limpar_texto import limpar_texto
from mostrar_top_5 import mostrar_top_5


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
