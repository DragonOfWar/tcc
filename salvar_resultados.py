import os

import json
import argumentos
import pandas as pd


COLUNAS = {
    "acuracia": 1,
    "kappa": 3,
    "tempo_treino": 5,
    "tempo_teste": 6,
    "tempo_total": 7,
}


def salvar_resultados_normal():
    # Ler o resultado do teste e criar um registro
    resultado = []
    with open(argumentos.CAM_RES_RAW) as arquivo_resultado_raw:
        resultado = arquivo_resultado_raw.read().splitlines()[-1].split(",")
    # Carregar csv
    dados_csv = {}
    if os.path.exists(argumentos.CAM_RES):
        dados_csv = pd.read_csv(argumentos.CAM_RES, index_col=0).to_dict()

    indice = int(argumentos.ITERACAO)

    for nome, indice_coluna in COLUNAS.items():
        if not nome in dados_csv:
            dados_csv[nome] = {}
        coluna = dados_csv[nome]
        coluna[indice] = float(resultado[indice_coluna])

    pd.DataFrame(data=dados_csv).to_csv(argumentos.CAM_RES, index_label="x")


def salvar_resultados_gridsearch(resultados, melhor_hp: dict):
    pd.DataFrame(resultados).to_csv(argumentos.CAM_RES_GS)
    with open(argumentos.CAM_HIP, "w") as arquivo:
        arquivo.write(json.dumps(melhor_hp))
