# Exercício 04 — Agente completo: a quarta camada de guardrail

**Aula 1 · leitura dirigida · prática livre**
Base: `codigos-demonstracao/leitura-dirigida/04-agente-completo.ipynb`
Vale para os capítulos **2 (Planning)**, **7 (Orquestração)** e **8 (Guardrails)**.

## Contexto

O pipeline tem três camadas de guardrail: formato, PII e LLM-as-judge. Falta a
mais óbvia numa mesa de crédito — **alçada**: acima de certo valor, ninguém
aprova sozinho.

## O que fazer

1. **Acrescente a camada (d) "alçada":** se `valor_credito` do cliente for maior
   que **5.000**, a decisão `APROVAR` deve ser **rebaixada** para
   `ANALISE_HUMANA`, independentemente da nota do juiz. Registre no output que a
   decisão foi rebaixada e por quê.
2. **Rode duas vezes** e registre as duas saídas.
3. **Rode com o cliente 112** (`CLIENTE = 112`), que pede R$ 392. A camada de
   alçada dispara? Deveria?
4. **Responda para você mesmo (3 linhas):** a `DECISAO` mudou entre as duas
   execuções? O que isso diz sobre levar o pipeline para produção?
   *(A questão 15 do [quiz da Aula 1](../QUIZ-AULA-01.md) cobra exatamente
   este raciocínio.)*

## Desafio

Faça a camada de alçada ser **configurável por propósito**: R$ 5.000 para
`negocio`, R$ 2.000 para `radio_tv`. Justifique em um comentário por que uma
política dessas pertence ao **código** e não ao **prompt**.
