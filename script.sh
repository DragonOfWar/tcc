#!/bin/bash

COMANDO_PYTHON="python3"
ARQUIVO_TESTES="adaptive_xgboost_example.py"
ARQUIVO_GRIDSEARCH="grid_cv.py"
MAX_REGISTROS=500000
QNT_X=5
DATASETS=("sea_a" "sea_g" "airlines" "elec" "agr_a" "agr_g" "hyper_f")
DATASET_GS="agr_a"
CLASSIFICADORES=("arf" "incremental" "axgb" "hat")
DIR_RESULTADOS_GS="resultados_gridsearch"

mkdir -p logs

EXECUTAR_GS=true
for i in $(seq $#)
do
    if [ "${!i}" = "--sem-gs" ]
    then
        EXECUTAR_GS=false
    fi
done

for classificador in ${CLASSIFICADORES[@]}
do
    if [ "$EXECUTAR_GS" = true ]
    then
        echo "Executando GridSearch no classificador $classificador"
        $COMANDO_PYTHON $ARQUIVO_GRIDSEARCH --classificador=$classificador --dataset=$DATASET_GS --maxregistros=$MAX_REGISTROS
    fi
    echo "Realizando experimentos"
    for dataset in ${DATASETS[@]}
    do
        for x in $(seq $QNT_X)
        do
            echo "Experimento usando $dataset ($x/$QNT_X)"
            $COMANDO_PYTHON $ARQUIVO_TESTES --classificador=$classificador --dataset=$dataset --hiperparametros="$DIR_RESULTADOS_GS/melhor_hp_${classificador}_$DATASET_GS.json" --iteracao=$x --maxregistros=$MAX_REGISTROS
        done
    done
done