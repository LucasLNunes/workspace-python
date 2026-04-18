from pathlib import Path


LETRAS = "abcdefghijklmnopqrstuvwxyz"
ARQUIVO_CSV = Path(__file__).resolve().parent.parent / "letter_frequency.csv"


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
