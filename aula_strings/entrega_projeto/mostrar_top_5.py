def mostrar_top_5(frequencia):
    lista = list(frequencia.items())
    lista.sort(key=lambda item: item[1], reverse=True)
    top_5 = lista[:5]

    print("5 letras mais frequentes no texto:")
    for letra, valor in top_5:
        print(f"{letra}: {valor:.2f}%")
