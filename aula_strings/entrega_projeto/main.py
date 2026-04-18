from analisar_url import analisar_url
from carregar_perfis import carregar_perfis


URLS = [
    "https://www.letras.mus.br/gusttavo-lima/assunto-que-doi/",
]


def main():
    print("IDENTIFICADOR DE IDIOMA POR FREQUENCIA DE LETRAS")
    print()

    perfis = carregar_perfis()
    if perfis is None:
        return

    for url in URLS:
        analisar_url(url, perfis)


if __name__ == "__main__":
    main()
