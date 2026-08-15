# Exercício 01 — Tool Use: uma terceira ferramenta

**Aula 1 · em sala · ~30 min, em duplas**
Base: notebook `01-tool-use.ipynb`

## Contexto

O catálogo da demo tem duas ferramentas. O atendimento agora quer perguntar
*"esse cliente já reclamou de alguma coisa?"* — e nenhuma das duas responde isso.

## O que fazer

1. **Acrescente ao catálogo** a ferramenta `listar_reclamacoes(cliente_id)`, que
   consulta a tabela `reclamacoes` e devolve `canal`, `texto`, `valor_contestado`
   e `status`.
r: Feito
2. **Troque a pergunta** por: *"O cliente 112 ligou irritado. Ele já registrou
   alguma reclamação com a gente?"*
r: Feito
3. **Rode e observe:** o modelo escolheu a ferramenta nova sem que você dissesse
   qual usar?
r: sim
4. **Responda por escrito (3 linhas):** o que teria acontecido se as três
   ferramentas tivessem descrições parecidas? O que, no catálogo, faz o modelo
   acertar a escolha?
r: Feito, o modelo teria dificuldade em responder de forma efetiva, talvez ele alucinaria dado a dificuldade na interpretação, é o campo "description", nele possui a instrução para o agente, indicando o que aquela tabela possui de informação "Lista as reclamacoes de um cliente (data, tipo, valor, cidade, canal)."
