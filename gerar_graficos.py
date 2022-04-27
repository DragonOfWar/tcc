import matplotlib.pyplot as plt
import csv
import os

# Config
QNT_ITERACOES = 5
CLASSIFICADORES = ["axgb", "incremental", "hat", "arf"]
DATASETS = ["agr_a", "agr_g", "airlines", "elec", "hyper_f", "sea_a", "sea_g"]

# Diretorios
def criar_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)


CAMINHO_RESULTADOS_RAW = "resultados_raw"
CAMINHO_FIGURAS_ACURACIAS = "graficos_acuracias"
CAMINHO_FIGURAS_KAPPA = "graficos_kappa"
criar_dir(CAMINHO_FIGURAS_ACURACIAS)
criar_dir(CAMINHO_FIGURAS_KAPPA)


# Gerar graficos das acuracias
def gerar_graficos(coluna, dir):
    for d in DATASETS:
        for i in range(1, QNT_ITERACOES):
            print(f"Processando {d} iteração {i}", end="\r")
            ys = {c: [] for c in CLASSIFICADORES}
            xs = []
            xs_pronto = False
            for c in CLASSIFICADORES:
                with open(
                    f"{CAMINHO_RESULTADOS_RAW}/resultados_{c}_{d}_{i}.csv", "r"
                ) as csvfile:
                    csvr = csv.reader(
                        # Preprocessar o csv pra remover os comentarios
                        filter(lambda l: l[0] != "#", csvfile),
                        delimiter=",",
                    )
                    next(csvr)  # ignorar primeira linha (cabeçalho)
                    for l in csvr:
                        if not xs_pronto:
                            xs.append(int(l[0]))
                        ys[c].append(float(l[coluna]))
                xs_pronto = True
            for c, y in ys.items():
                plt.plot(xs, y, label=c)
            plt.xlabel("acuracia")
            plt.ylabel("amostras")
            plt.legend()
            plt.grid()
            plt.savefig(f"{dir}/{d}_{i}.png")
            plt.clf()


gerar_graficos(2, CAMINHO_FIGURAS_ACURACIAS)
gerar_graficos(4, CAMINHO_FIGURAS_KAPPA)
