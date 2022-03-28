#!/bin/bash

COMANDO_PYTHON="python"
ARQUIVO_TESTES="adaptive_xgboost_example.py"
ARQUIVO_GRIDSEARCH="grid_cv.py"
QNT_X=10
DATASETS=("sea_a" "sea_g" "airlines" "elec" "agr_a" "agr_g" "hyper_f")
DATASET_GS="agr_a"
CLASSIFICADORES=("arf" "incremental" "axgb" "hat")
DIR_RESULTADOS_GS="resultados_gridsearch"

mkdir -p logs

for classificador in ${CLASSIFICADORES[@]}
do
    echo "Executando GridSearch no classificador $classificador"
    $COMANDO_PYTHON $ARQUIVO_GRIDSEARCH --classificador=$classificador --dataset=$DATASET_GS 
    echo "Realizando experimentos"
    for dataset in ${DATASETS[@]}
    do
        for x in $(seq $QNT_X)
        do
            echo "Experimento usando $dataset ($x/$QNT_X)"
            $COMANDO_PYTHON $ARQUIVO_TESTES --classificador=$classificador --dataset=$dataset --hiperparametros="$DIR_RESULTADOS_GS/melhor_hp_${classificador}_$DATASET_GS.json" --iteracao=$x 
        done
    done
done