import sys
import itertools
import os

CLASSIFICADORES = [
    "afxgb",
    "afxgb_r",
    "afxgb_adwin",
    "afxgb_adwin_r",
    "hat",
    "arf",
    # "axgb",
]

DATASETS = [
    "sea_a",
    "sea_g",
    "airlines",
    "elec",
    "agr_a",
    "agr_g",
    "hyper_f",
]

DIRETORIOS = [
    "resultados_gridsearch",
    "hiperparametros",
    "resultados_raw",
    "resultados",
    "graficos_acuracias",
    "graficos_kappa",
]

QNT_X = 5

DATASET_GRIDSEARCH = "agr_a"

DIR_RESULTADOS_GRIDSEARCH = DIRETORIOS[0]
DIR_HIPERPARAMETROS = DIRETORIOS[1]
DIR_RESULTADOS_RAW = DIRETORIOS[2]
DIR_RESULTADOS = DIRETORIOS[3]
DIR_FIGURAS_ACURACIAS = DIRETORIOS[4]
DIR_FIGURAS_KAPPA = DIRETORIOS[5]

CAMINHOS_HIPERPARAMETROS = {
    c: f"{DIR_HIPERPARAMETROS}/{DATASET_GRIDSEARCH}_{c}.json" for c in CLASSIFICADORES
}
CAMINHOS_RESULTADOS = {}
CAMINHOS_RESULTADOS_RAW = {}
CAMINHOS_RESULTADOS_GS = {}


def criar_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)


for c, d in itertools.product(CLASSIFICADORES, DATASETS):
    if not CAMINHOS_RESULTADOS.get(d):
        CAMINHOS_RESULTADOS[d] = {}

    diretorio = f"{DIR_RESULTADOS}/{d}"
    DIRETORIOS.append(diretorio)

    CAMINHOS_RESULTADOS[d][c] = f"{diretorio}/resultados_{d}_{c}.csv"

    if not CAMINHOS_RESULTADOS_GS.get(d):
        CAMINHOS_RESULTADOS_GS[d] = {}

    diretorio = f"{DIR_RESULTADOS_GRIDSEARCH}/{d}"
    DIRETORIOS.append(diretorio)

    CAMINHOS_RESULTADOS_GS[d][c] = f"{diretorio}/resultados_gs_{d}_{c}.csv"

for c, d, i in itertools.product(CLASSIFICADORES, DATASETS, range(1, QNT_X + 1)):
    if not CAMINHOS_RESULTADOS_RAW.get(d):
        CAMINHOS_RESULTADOS_RAW[d] = {}
    if not CAMINHOS_RESULTADOS_RAW[d].get(i):
        CAMINHOS_RESULTADOS_RAW[d][i] = {}

    diretorio = f"{DIR_RESULTADOS_RAW}/{d}/"
    DIRETORIOS.append(diretorio)
    diretorio = f"{DIR_RESULTADOS_RAW}/{d}/{d}_{i}"
    DIRETORIOS.append(diretorio)

    caminho = f"{diretorio}/resultados_raw_{d}_{i}_{c}.csv"
    CAMINHOS_RESULTADOS_RAW[d][i][c] = caminho

for c in DIRETORIOS:
    criar_dir(c)


def main() -> None:
    retornos = {
        "classificadores": "\n".join(CLASSIFICADORES),
        "datasets": "\n".join(DATASETS),
        "diretorios": "\n".join(DIRETORIOS),
        "dataset_gridsearch": DATASET_GRIDSEARCH,
        "dir_resultados_gridsearch": DIR_RESULTADOS_GRIDSEARCH,
        "dir_hiperparametros": DIR_HIPERPARAMETROS,
        "dir_resultados_raw": DIR_RESULTADOS_RAW,
        "dir_resultados": DIR_RESULTADOS,
        "dir_figuras_kappa": DIR_FIGURAS_KAPPA,
        "dir_figuras_acuracias": DIR_FIGURAS_ACURACIAS,
        "qnt_x": QNT_X,
    }
    res = retornos.get(sys.argv[1], "erro")
    if res == "erro":
        print(f"Erro: {sys.argv[1]} é um argumento inválido")
        sys.exit(1)

    print(res)


if __name__ == "__main__":
    main()
