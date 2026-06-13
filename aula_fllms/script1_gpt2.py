import torch
import pandas as pd
import matplotlib.pyplot as plt
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Modelo em português
modelo_nome = "pierreguillou/gpt2-small-portuguese"

# Carrega tokenizer e modelo
# Obs.: a primeira execução baixa o modelo do Hugging Face.
tokenizer = GPT2Tokenizer.from_pretrained(modelo_nome)
model = GPT2LMHeadModel.from_pretrained(modelo_nome)
model.eval()

frase = "A UFPR é uma universidade brasileira que"
max_passos = 30
top_k = 10
temperature = 0.1

historico = []

for passo in range(1, max_passos + 1):
    inputs = tokenizer(frase, return_tensors="pt")

    with torch.no_grad():
        outputs = model(input_ids=inputs["input_ids"])

    # Logits do próximo token
    logits = outputs.logits.detach()[0, -1, :]
    logits = logits / temperature

    # Distribuição de probabilidade
    probs = torch.nn.functional.softmax(logits, dim=0)

    # Tokens mais prováveis
    top = torch.topk(probs, k=top_k, dim=0)

    top_probs = top.values.detach().cpu().numpy()
    top_ids = top.indices.detach().cpu().numpy()
    top_tokens = [tokenizer.decode(int(token_id)) for token_id in top_ids]

    df = pd.DataFrame({
        "token": top_tokens,
        "prob": top_probs
    }).sort_values("prob")

    # Gráfico da distribuição top-k
    plt.figure(figsize=(8, 5))
    plt.barh(df["token"], df["prob"])
    plt.title(f"Passo {passo} - distribuição do próximo token")
    plt.xlabel("Probabilidade")
    plt.ylabel("Próximo token")
    plt.tight_layout()
    plt.show()

    # Sorteio do próximo token, como em geração autoregressiva
    token_sorteado_id = torch.multinomial(probs, num_samples=1)
    novo_token = tokenizer.decode(int(token_sorteado_id.item()))

    historico.append({
        "passo": passo,
        "frase_antes": frase,
        "token_escolhido": novo_token
    })

    frase = frase + novo_token

    print("\n----------------------------------")
    print("Passo:", passo)
    print("Token escolhido:", novo_token)
    print("Texto atual:\n", frase)


resultado = pd.DataFrame(historico)

print("\nHistórico:")
print(resultado)

print("\n\nTexto final:")
print(frase)
