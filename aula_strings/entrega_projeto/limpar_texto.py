import re
import unicodedata


LETRAS = "abcdefghijklmnopqrstuvwxyz"


def limpar_texto(texto):
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(letra for letra in texto if unicodedata.category(letra) != "Mn")
    texto = "".join(letra for letra in texto if letra in LETRAS)

    print(f"Texto limpo: {len(texto)} caracteres")

    return texto
