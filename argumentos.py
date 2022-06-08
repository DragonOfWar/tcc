import argparse
import config
import json
import sys
import config

parser = argparse.ArgumentParser()

parser.add_argument(
    "--classificador",
    "-c",
    help="Nome do classificador",
    type=str,
    default="axgb",
)
parser.add_argument(
    "--dataset",
    "-d",
    help="Nome do dataset",
    type=str,
    default="sea_a",
)
parser.add_argument(
    "--hiperparametros",
    "-p",
    help="Caminho do arquivos de hiper-parâmetros do classificador em JSON",
    type=str,
    default="",
)
parser.add_argument(
    "--iteracao",
    "-i",
    help="Número da iteração",
    type=int,
    default=1,
)
parser.add_argument(
    "--maxregistros",
    "-m",
    help="Máximo do registros",
    type=int,
    default=1_000_000,
)
parser.add_argument(
    "--randomstate",
    "-r",
    help="Seed do gerador de datasets",
    type=int,
    default=1,
)
parser.add_argument(
    "--qntdrifts",
    "-q",
    help="Quantidade de drifts",
    type=int,
    default=3,
)


args = parser.parse_args()

CLASSIFICADOR = args.classificador
DATASET = args.dataset
HIPER_PARAMETROS = {}
ITERACAO = args.iteracao
MAX_REGISTROS = args.maxregistros
RANDOM_STATE = args.randomstate
QNT_DRIFTS = args.qntdrifts

CAM_HIP = config.CAMINHOS_HIPERPARAMETROS[CLASSIFICADOR]
CAM_RES = config.CAMINHOS_RESULTADOS[DATASET][CLASSIFICADOR]
CAM_RES_GS = config.CAMINHOS_RESULTADOS_GS[DATASET][CLASSIFICADOR]
CAM_RES_RAW = config.CAMINHOS_RESULTADOS_RAW[DATASET][ITERACAO][CLASSIFICADOR]

caminho_hp = args.hiperparametros
if caminho_hp == "":
    caminho_hp = config.CAMINHOS_HIPERPARAMETROS[CLASSIFICADOR]
try:
    with open(caminho_hp) as arquivo:
        HIPER_PARAMETROS = json.loads(arquivo.read())
except IOError:
    print(f"{sys.argv[0]} erro: arquivo {caminho_hp} não existe")
except json.JSONDecodeError:
    print(
        f"{sys.argv[0]} erro: não foi possível ler {caminho_hp} pois o arquivo não está formatado como JSON corretamente"
    )
