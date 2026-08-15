# Exercício 02 — Reflection: mexendo no critério de parada

**Aula 1 · em sala · ~30 min, em duplas**
Base: notebook `02-reflection.ipynb`

## Contexto

Na demo, o laço converge no ciclo 2: o crítico acha uma violação, o gerador
corrige, o segundo crítico aprova. Vamos tornar a política mais exigente e ver o
que acontece com o critério de parada.

## O que fazer

1. **Acrescente um 5º item à política:** *"(5) toda resposta deve informar o canal
   oficial para acompanhamento do protocolo (app ou telefone 0800)."*
2. **Rode** e conte em quantos ciclos o laço converge agora.
3. **Baixe `T_MAX` para 1** e rode de novo. O laço termina por **aprovação** ou por
   **limite**? Como você sabe, olhando só a saída?
4. **Responda (4 linhas):** qual dos dois critérios de parada você monitoraria em
   produção, e o que significaria vê-lo disparar com frequência?
