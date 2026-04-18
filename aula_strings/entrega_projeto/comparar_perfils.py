import math


LETRAS = "abcdefghijklmnopqrstuvwxyz"


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
