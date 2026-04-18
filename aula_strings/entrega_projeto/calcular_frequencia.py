LETRAS = "abcdefghijklmnopqrstuvwxyz"


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
