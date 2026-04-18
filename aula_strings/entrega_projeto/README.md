# Identificador de Idioma por Frequencia de Letras

Esta pasta contem a versao modularizada do projeto.

O programa baixa o conteudo de uma pagina web, tenta extrair o texto principal, limpa esse texto, calcula a frequencia das letras e compara com perfis de idiomas usando distancia euclidiana.

## Objetivo

Organizar o projeto em funcoes separadas, deixando cada arquivo responsavel por uma parte do processo.

## Estrutura dos arquivos

- `main.py`: arquivo principal que inicia o programa
- `analisar_url.py`: junta todas as etapas da analise
- `baixar_texto.py`: baixa o HTML da pagina com `requests`
- `extrair_texto_principal.py`: tenta extrair o bloco principal da letra
- `limpar_texto.py`: remove tags, acentos e tudo que nao for letra
- `calcular_frequencia.py`: calcula a frequencia percentual das letras
- `carregar_perfis.py`: le os perfis de idioma do arquivo CSV
- `comparar_perfils.py`: compara o texto com os idiomas usando distancia euclidiana
- `mostrar_top_5.py`: mostra as 5 letras mais frequentes

## Fluxo do programa

Quando `main.py` e executado, o programa faz o seguinte:

1. carrega os perfis de idioma
2. percorre a lista de URLs
3. baixa o HTML da pagina
4. tenta extrair o texto principal
5. mostra o texto antes do tratamento
6. limpa o texto
7. mostra o texto depois do tratamento
8. calcula a frequencia das letras
9. compara com os perfis do CSV
10. mostra o idioma mais provavel

## Arquivo de perfis

Os perfis sao lidos do arquivo:

- [letter_frequency.csv](/home/espinf/llnunes/aulas_python/aula_strings/letter_frequency.csv)

Importante:

- esse arquivo nao fica dentro de `entrega_projeto`
- ele fica na pasta pai `aula_strings`
- o modulo `carregar_perfis.py` ja esta configurado para buscar esse arquivo no lugar certo

## Biblioteca usada

Instale a dependencia:

```bash
pip install requests
```

## Como executar

Entre na pasta:

```bash
cd /home/espinf/llnunes/aulas_python/aula_strings/entrega_projeto
```

Depois execute:

```bash
python3 main.py
```

O programa nao pede `input`. A URL fica definida dentro de `main.py`.

## URL atual

No momento, a URL configurada e:

- `https://www.letras.mus.br/gusttavo-lima/assunto-que-doi/`

Se quiser testar outra pagina, basta alterar a lista `URLS` em [main.py](/home/espinf/llnunes/aulas_python/aula_strings/entrega_projeto/main.py).

## Saida do programa

Durante a execucao, o programa mostra:

- a URL analisada
- parte do texto antes do tratamento
- o tamanho do texto limpo
- parte do texto depois do tratamento
- o idioma encontrado
- o grau de similaridade
- a distancia euclidiana
- a quantidade de letras analisadas
- as 5 letras mais frequentes

## Observacao sobre o site de musica

Para paginas do `letras.mus.br`, o programa tenta extrair primeiro o bloco:

```html
<div class="lyric-original"> ... </div>
```

Isso ajuda a analisar a letra da musica em si, em vez de analisar menu, rodape e outros textos da pagina.

## Limitacoes

- a extracao do texto principal e simples
- alguns sites podem bloquear requisicoes feitas por script
- o resultado depende da qualidade dos perfis presentes no CSV

## Resumo da modularizacao

A modularizacao foi feita para:

- deixar o codigo mais organizado
- separar responsabilidades
- facilitar manutencao
- facilitar testes e leitura do projeto
