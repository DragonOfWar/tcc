#!/bin/bash

COMANDO_PYTHON="python"
ARQUIVO_TESTES="adaptive_xgboost_example.py"
ARQUIVO_GRIDSEARCH="grid_cv.py"
QNT_X=3
DATASETS=("sea_a" "sea_g" "airlines" "elec" "agr_a" "agr_g")
CLASSIFICADORES=("axgb" "incremental")
DIR_RESULTADOS_GS="resultados_gridsearch"


for dataset in ${DATASETS[@]}
do
    for classificador in ${CLASSIFICADORES[@]}
    do
        $COMANDO_PYTHON $ARQUIVO_GRIDSEARCH --classificador=$classificador --dataset=$dataset
        
        for x in $(seq $QNT_X)
        do
            $COMANDO_PYTHON $ARQUIVO_TESTES --classificador=$classificador --dataset=$dataset --hiperparametros="$DIR_RESULTADOS_GS/melhor_hp_${classificador}_${dataset}.json" --iteracao=$x
        done
    done
done