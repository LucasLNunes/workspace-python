# install-python.R — prepara o ambiente Python do curso.
#
# Roda uma vez, e resolve o erro mais comum de quem usa as demos .py dentro do
# RStudio:
#
#     ModuleNotFoundError: No module named 'matplotlib'
#
# O motivo do erro: o reticulate escolhe sozinho algum Python do sistema, e
# esse Python nao tem as dependencias do curso. Este script cria um ambiente
# dedicado, instala o requirements.txt nele e aponta o reticulate para la.
#
#   No RStudio:   source("install-python.R")
#   No terminal:  Rscript install-python.R
#
# Depois de rodar, REINICIE A SESSAO DE R (Session > Restart R, ou Ctrl+Shift+F10).
#
# NOS PCS DO LABORATORIO: cada aluno roda este script uma vez, com o proprio
# login. O ambiente vai para o ~/.virtualenvs DELE, e o .Rprofile do projeto
# encontra pelo NOME, nao por caminho. Nenhum arquivo do repositorio guarda
# /home/<alguem>, entao a mesma pasta serve para a turma inteira.

AMBIENTE <- "genai" # nome do virtualenv

# Faixa de versoes do Python homologada para o curso: 3.11 e 3.12.
# As duas foram testadas rodando as 7 demos .py de ponta a ponta.
# Deixamos um teto de proposito: versoes mais novas (3.13, 3.14) costumam
# chegar antes que as rodas binarias de pandas/numpy/matplotlib, e o aluno
# acaba compilando pacote na vespera da aula.
PY_FAIXA    <- ">=3.11,<3.13"
PY_ROTULO   <- "3.11 ou 3.12"

# Escape: se voce quiser um Python especifico, aponte antes de rodar.
#   Sys.setenv(CURSO_PYTHON = "/caminho/para/python3.12")
PY_ESCOLHIDO <- Sys.getenv("CURSO_PYTHON", "")

# ---------------------------------------------------------------------------
# 0. reticulate
# ---------------------------------------------------------------------------
if (!requireNamespace("reticulate", quietly = TRUE)) {
  message("[1/6] Instalando o pacote reticulate...")
  install.packages("reticulate", repos = "https://cloud.r-project.org")
}
if (!requireNamespace("reticulate", quietly = TRUE)) {
  stop("[ERRO] Nao foi possivel instalar o reticulate.", call. = FALSE)
}
message("[1/6] reticulate ", as.character(packageVersion("reticulate")), " OK")

# ---------------------------------------------------------------------------
# 1. Raiz do projeto e requirements.txt (a UNICA fonte de verdade das versoes)
# ---------------------------------------------------------------------------
raiz <- tryCatch(here::here(), error = function(e) normalizePath("."))
req  <- file.path(raiz, "requirements.txt")
if (!file.exists(req)) {
  stop("[ERRO] requirements.txt nao encontrado em ", raiz,
       "\nAbra o curso-agentic-genai.Rproj antes de rodar este script.",
       call. = FALSE)
}
message("[2/6] Projeto em ", raiz)

# ---------------------------------------------------------------------------
# 2. Um Python-base para servir de molde ao ambiente
# ---------------------------------------------------------------------------
#' Versao "3.11" de um interpretador, para comparar e para exibir.
versao_de <- function(py) {
  v <- suppressWarnings(system2(py, c("-c", shQuote(
    "import sys; print('%d.%d' % sys.version_info[:2])")),
    stdout = TRUE, stderr = FALSE))
  if (length(v)) trimws(v[1]) else NA_character_
}
na_faixa <- function(v) !is.na(v) && v %in% c("3.11", "3.12")

if (nzchar(PY_ESCOLHIDO)) {
  base_py <- PY_ESCOLHIDO
  if (!file.exists(base_py)) {
    stop("[ERRO] CURSO_PYTHON aponta para um caminho que nao existe: ", base_py, call. = FALSE)
  }
  v <- versao_de(base_py)
  if (!na_faixa(v)) {
    warning("CURSO_PYTHON e a versao ", v, ", fora da faixa homologada (", PY_ROTULO,
            "). Seguindo assim mesmo, porque voce pediu explicitamente.", call. = FALSE)
  }
  message("[3/6] Python-base (CURSO_PYTHON): ", base_py, "  [", v, "]")
} else {
  base_py <- tryCatch(reticulate::virtualenv_starter(version = PY_FAIXA),
                      error = function(e) NULL)
  if (is.null(base_py) || !length(base_py) || !nzchar(base_py)) {
    # Nada na faixa preferida. Em vez de travar, aceitamos qualquer 3.11+:
    # o Debian 13 dos laboratorios, por exemplo, so traz o 3.13 de fabrica.
    base_py <- tryCatch(reticulate::virtualenv_starter(version = ">=3.11"),
                        error = function(e) NULL)
    if (!is.null(base_py) && length(base_py) && nzchar(base_py)) {
      message("[3/6] Sem Python ", PY_ROTULO, " no sistema. Usando ",
              versao_de(base_py), ", que tambem roda as demos.")
    }
  }
  if (is.null(base_py) || !length(base_py) || !nzchar(base_py)) {
    disponiveis <- tryCatch(reticulate::virtualenv_starter(all = TRUE),
                            error = function(e) NULL)
    stop("[ERRO] Nenhum Python ", PY_ROTULO, " encontrado no sistema.\n",
         if (!is.null(disponiveis) && nrow(disponiveis))
           paste0("Encontrados apenas:\n  ",
                  paste(disponiveis$path, collapse = "\n  "), "\n") else "",
         "\nInstale um deles e rode de novo. Por exemplo:\n",
         "  sudo apt install python3-venv      (Debian/Ubuntu)\n",
         "  pyenv install 3.12                 (pyenv)\n",
         "  brew install python@3.12           (macOS)\n",
         "\nOu aponte um interpretador seu antes de rodar o script:\n",
         "  Sys.setenv(CURSO_PYTHON = \"/caminho/para/python3.12\")",
         call. = FALSE)
  }
  message("[3/6] Python-base: ", base_py, "  [", versao_de(base_py), "]")
}

# No Debian/Ubuntu o modulo venv vem em pacote separado (python3-venv). Sem ele,
# a criacao falha com "ensurepip is not available", que nao diz o que fazer.
tem_venv <- suppressWarnings(system2(base_py, c("-c", shQuote("import ensurepip")),
                                     stdout = FALSE, stderr = FALSE)) == 0
if (!tem_venv) {
  stop("[ERRO] O Python encontrado nao consegue criar ambientes virtuais.\n",
       "  ", base_py, "\n",
       "No Debian/Ubuntu, isso se resolve instalando o pacote do venv:\n",
       "  sudo apt install python3-venv\n",
       "Nos PCs do laboratorio, isso precisa do administrador da maquina.",
       call. = FALSE)
}

# ---------------------------------------------------------------------------
# 3. O ambiente dedicado
# Fica em ~/.virtualenvs, e NAO dentro da pasta do curso: a pasta esta no
# Dropbox, e um virtualenv la dentro sao milhares de arquivos para sincronizar.
# ---------------------------------------------------------------------------
if (reticulate::virtualenv_exists(AMBIENTE)) {
  v_atual <- versao_de(reticulate::virtualenv_python(AMBIENTE))
  # Recriamos em dois casos: ambiente fora da faixa (ex.: criado em 3.13 antes
  # deste ajuste), que seria reaproveitado em silencio; ou CURSO_PYTHON pedindo
  # uma versao diferente da que esta la. Fora isso, reaproveita: trocar de
  # versao a cada execucao so faria o aluno reinstalar tudo sem motivo.
  pediu_outra <- nzchar(PY_ESCOLHIDO) && !identical(v_atual, versao_de(base_py))
  if (na_faixa(v_atual) && !pediu_outra) {
    message("[4/6] Ambiente '", AMBIENTE, "' ja existe em Python ", v_atual,
            ", reaproveitando.")
  } else {
    motivo <- if (pediu_outra)
      paste0("CURSO_PYTHON pede ", versao_de(base_py), " e o ambiente esta em ", v_atual)
    else
      paste0("esta em Python ", v_atual, ", fora da faixa ", PY_ROTULO)
    message("[4/6] Ambiente '", AMBIENTE, "' ", motivo, ". Recriando...")
    reticulate::virtualenv_create(AMBIENTE, python = base_py, packages = NULL,
                                  force = TRUE)
  }
} else {
  message("[4/6] Criando o ambiente '", AMBIENTE, "'...")
  reticulate::virtualenv_create(AMBIENTE, python = base_py, packages = NULL)
}

# ---------------------------------------------------------------------------
# 4. As dependencias, lidas do requirements.txt
# Nunca instale os pacotes soltos (`pip install mcp`): o requirements.txt fixa
# o SDK do MCP na linha 1.x de proposito -- a 2.0 quebra a demo da Aula 2.
# ---------------------------------------------------------------------------
message("[5/6] Instalando as dependencias do requirements.txt (pode demorar)...")
reticulate::virtualenv_install(AMBIENTE, requirements = req)

py <- reticulate::virtualenv_python(AMBIENTE)

# ---------------------------------------------------------------------------
# 5. Conferencia: cada modulo que as demos importam
# ---------------------------------------------------------------------------
modulos <- c("openai", "dotenv", "pydantic", "mcp", "networkx", "pandas", "matplotlib")
codigo <- sprintf(
  "import importlib.util as u, sys
faltando = [m for m in %s if u.find_spec(m) is None]
import importlib.metadata as md
try: v = md.version('mcp')
except Exception: v = '?'
print('PYTHON ' + sys.version.split()[0]); print('MCP ' + v)
print('FALTANDO ' + (','.join(faltando) if faltando else '-'))",
  paste0("[", paste0("'", modulos, "'", collapse = ", "), "]"))

saida <- suppressWarnings(system2(py, c("-c", shQuote(codigo)), stdout = TRUE, stderr = TRUE))
faltando <- sub("^FALTANDO ", "", grep("^FALTANDO ", saida, value = TRUE))
versao_py  <- sub("^PYTHON ", "", grep("^PYTHON ", saida, value = TRUE))
versao_mcp <- sub("^MCP ", "", grep("^MCP ", saida, value = TRUE))

message("[6/6] Conferencia:")
message("      python .... ", if (length(versao_py)) versao_py else "?")
message("      mcp ....... ", if (length(versao_mcp)) versao_mcp else "?",
        "  (tem de ser 1.x; a 2.0 quebra a demo 01-mcp.py)")
if (!length(faltando) || identical(faltando, "-")) {
  message("      modulos ... os ", length(modulos), " do curso estao disponiveis")
} else {
  warning("Ainda faltam modulos: ", faltando, call. = FALSE)
  message("      saida do Python:\n", paste(saida, collapse = "\n"))
}

# ---------------------------------------------------------------------------
# 6. Fazer o RStudio usar este ambiente, SEM caminho fixo
#
# Quem faz a ligacao e o .Rprofile do projeto, que aponta o reticulate para o
# NOME do ambiente. O reticulate resolve o nome em ~/.virtualenvs do usuario
# logado, entao o mesmo arquivo serve para qualquer aluno em qualquer maquina
# do laboratorio. Nada aqui grava /home/<alguem> em lugar nenhum.
# ---------------------------------------------------------------------------
rprof <- file.path(raiz, ".Rprofile")
if (!file.exists(rprof) || !any(grepl("RETICULATE_PYTHON_ENV", readLines(rprof, warn = FALSE)))) {
  message("\nATENCAO: o .Rprofile do projeto nao aponta para o ambiente do curso.")
  message("Ele deveria conter, entre outras coisas:")
  message('  Sys.setenv(RETICULATE_PYTHON_ENV = "', AMBIENTE, '")')
  message("O arquivo faz parte do repositorio; se sumiu, recupere com: git checkout .Rprofile")
} else {
  message("\nOK: o .Rprofile do projeto aponta para o ambiente '", AMBIENTE, "'.")
}

# Limpeza: versoes antigas deste script gravavam um caminho ABSOLUTO no
# .Renviron. Numa maquina de laboratorio esse caminho aponta para o home de
# outra pessoa, e ele tem precedencia sobre o nome do ambiente. Removemos.
renv_path <- file.path(raiz, ".Renviron")
if (file.exists(renv_path)) {
  linhas <- readLines(renv_path, warn = FALSE)
  fixas  <- grepl("^\\s*RETICULATE_PYTHON\\s*=", linhas)
  if (any(fixas)) {
    cabecalho <- grepl("^\\s*#\\s*Ambiente Python do curso", linhas)
    writeLines(linhas[!(fixas | cabecalho)], renv_path)
    message("Removida do .Renviron a linha RETICULATE_PYTHON com caminho fixo",
            " (agora quem resolve e o .Rprofile, pelo nome).")
  }
}

message("\n", strrep("-", 68))
message("REINICIE A SESSAO DE R para o reticulate assumir o ambiente novo.")
message("  RStudio: Session > Restart R  (Ctrl+Shift+F10)")
message("")
message("Para conferir depois do restart:  reticulate::py_config()")
message("Para rodar uma demo no terminal:")
message("  ", py, " aula-01-agentic-workflows/codigos-demonstracao/01-tool-use.py")
message(strrep("-", 68))
