import os
import argumentos
import pandas as pd

# Config
DIR_RESULTADOS_RAW = "resultados_raw"
DIR_RESULTADOS = "resultados"
NOME_ARQUIVO = f"resultados_{argumentos.CLASSIFICADOR}_{argumentos.DATASET}_{argumentos.HYPERPARAMETRO}"

# Gerar caminhos
caminho_resultado = f"{DIR_RESULTADOS}/{NOME_ARQUIVO}"
caminho_resultado_raw = f"{DIR_RESULTADOS_RAW}/{NOME_ARQUIVO}_{argumentos.VALOR_HYPERPARAMETRO}_{argumentos.ITERACAO}"


def salvar():
    # Ler o resultado do teste e criar um registro
    resultado = []
    with open(caminho_resultado_raw) as arquivo_resultado_raw:
        resultado = arquivo_resultado_raw.read().splitlines()[-1].split(",")
    # Carregar csv
    dados_csv = {}
    if os.path.exists(caminho_resultado):
        dados_csv = pd.read_csv(caminho_resultado, index_col=0).to_dict()

    nome_coluna_acuracia = f"acuracia_{argumentos.VALOR_HYPERPARAMETRO}"
    nome_coluna_tempo = f"tempo_total_{argumentos.VALOR_HYPERPARAMETRO}"

    # Adicionar registro
    if not nome_coluna_acuracia in dados_csv:
        dados_csv[nome_coluna_acuracia] = {}
    if not nome_coluna_tempo in dados_csv:
        dados_csv[nome_coluna_tempo] = {}

    indice = int(argumentos.ITERACAO)
    coluna_acuracia = dados_csv[nome_coluna_acuracia]
    coluna_tempo = dados_csv[nome_coluna_tempo]
    coluna_acuracia[indice] = float(resultado[1])
    coluna_tempo[indice] = float(resultado[5])

    pd.DataFrame(data=dados_csv).to_csv(caminho_resultado, index_label="x")
