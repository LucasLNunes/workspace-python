import re


def extrair_texto_principal(texto):
    bloco_musica = re.search(
        r'<div class="lyric-original">(.*?)</div>',
        texto,
        re.DOTALL
    )

    if bloco_musica:
        texto = bloco_musica.group(1)

    return texto
