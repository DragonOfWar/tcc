import matplotlib.pyplot as plt
import scikit_posthocs as sp
import numpy as np
import csv
import sys
import config
from scipy import stats

NAO_FAZER_GRAFICO = "--semgrafico" in sys.argv
NAO_FAZER_FRIEDMAN = "--semfriedman" in sys.argv
# Executa acuracia e kappa pelo resultados_raw ao invés pelo resultados (não ira usar as medias)
FRIEDMAN_TOTAL = "--friedmantotal" in sys.argv

# Gerar graficos das acuracias
def gerar_graficos(coluna, dir, nome):
    for d in config.DATASETS:
        for i in range(1, config.QNT_X + 1):
            print(f"Gerando gráfico de {nome}: processando {d} iteração {i}", end="\r")
            ys = {c: [] for c in config.CLASSIFICADORES}
            xs = []
            xs_pronto = False
            for c in config.CLASSIFICADORES:
                with open(config.CAMINHOS_RESULTADOS_RAW[d][i][c], "r") as csvfile:
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
            plt.xlabel("amostras")
            plt.ylabel(nome)
            plt.legend()
            plt.grid()
            plt.savefig(f"{dir}/{d}_{i}.png")
            plt.clf()


if not NAO_FAZER_GRAFICO:
    gerar_graficos(2, config.DIR_FIGURAS_ACURACIAS, "acuracia")
    gerar_graficos(4, config.DIR_FIGURAS_KAPPA, "kappa")

if not NAO_FAZER_FRIEDMAN:
    # Executar teste de friedman-nemenyi nas acuracias
    acuracias = {c: [] for c in config.CLASSIFICADORES}
    kappas = {c: [] for c in config.CLASSIFICADORES}
    tempos = {c: [] for c in config.CLASSIFICADORES}

    COLUNA_ACURACIA = 2
    COLUNA_KAPPA = 4
    COLUNA_TEMPO = 5

    # Ler resultados
    for d in config.DATASETS:
        for c in config.CLASSIFICADORES:
            if FRIEDMAN_TOTAL:
                with open(config.CAMINHOS_RESULTADOS[d][c]) as csvfile:
                    csvr = csv.reader(csvfile, delimiter=",")
                    next(csvr)  # Descartar primeira linha (cabeçalho)
                    for l in csvr:
                        tempos[c].append(l[COLUNA_TEMPO])
                for i in range(1, config.QNT_X + 1):
                    with open(config.CAMINHOS_RESULTADOS_RAW[d][i][c], "r") as csvfile:
                        csvr = csv.reader(
                            # Preprocessar o csv pra remover os comentarios
                            filter(lambda l: l[0] != "#", csvfile),
                            delimiter=",",
                        )
                        next(csvr)  # ignorar primeira linha (cabeçalho)
                        for l in csvr:
                            acuracias[c].append(l[COLUNA_ACURACIA])
                            kappas[c].append(l[COLUNA_KAPPA])
                continue

            with open(config.CAMINHOS_RESULTADOS[d][c]) as csvfile:
                csvr = csv.reader(csvfile, delimiter=",")
                next(csvr)  # Descartar primeira linha (cabeçalho)
                for l in csvr:
                    acuracias[c].append(l[COLUNA_ACURACIA])
                    kappas[c].append(l[COLUNA_KAPPA])
                    tempos[c].append(l[COLUNA_TEMPO])

    # Teste
    fsr_a = stats.friedmanchisquare(*list(acuracias.values()))
    fsr_k = stats.friedmanchisquare(*list(kappas.values()))
    fsr_t = stats.friedmanchisquare(*list(tempos.values()))

    print("FSR Acuracias: ", fsr_a)
    print("FSR Kappa: ", fsr_k)
    print("FSR Tempos: ", fsr_t)

    data_a = np.array(list(acuracias.values()))
    data_k = np.array(list(kappas.values()))
    data_t = np.array(list(tempos.values()))

    print(sp.posthoc_nemenyi_friedman(data_a.T))
    print(sp.posthoc_nemenyi_friedman(data_k.T))
    print(sp.posthoc_nemenyi_friedman(data_t.T))
