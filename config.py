import sys

CLASSIFICADORES = [
    "gustavo",
    "gustavo_r",
    "gustavo_adwin",
    "gustavo_adwin_r",
    "htc",
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


def main() -> None:
    res = None
    if sys.argv[1] == "classificadores":
        res = CLASSIFICADORES
    elif sys.argv[1] == "datasets":
        res = DATASETS

    if res:
        print("\n".join(res))


if __name__ == "__main__":
    main()
