# Exercício 03 — Memória: o anel visto de outro ângulo

**Aula 1 · em sala · ~25 min, em duplas**
Base: notebook `03-memoria.ipynb`

## Contexto

A demo investiga o cliente 256 e recupera 14 dos 17 fatos do grafo. Vamos mexer
nos dois parâmetros que controlam memória: **o que entra na janela** e **o que é
recuperado**.

## O que fazer

1. **Troque o investigado** de 256 para **201**. Quantos fatos são recuperados?
   Que grupo aparece?
2. **Troque para 999** (um cliente que não compartilha recurso nenhum). O que o
   script faz? Isso é um bom comportamento?
3. **Mude `JANELA` de 4 para 2** e observe a etapa [1]. A partir de qual mensagem
   o agente já esqueceu o motivo do atendimento? *(O valor inicial é 4 — confira
   antes de mexer.)*
4. **Responda (3 linhas):** por que recuperamos o **componente conexo inteiro** do
   investigado, em vez de só os vizinhos diretos dele? O que se perderia?

---
