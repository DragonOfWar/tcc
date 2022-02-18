#!/bin/bash

COMANDO_PYTHON="python"
ARQUIVO_PYTHON="adaptive_xgboost_example.py"
QNT_X=3
DATASETS=("sea" "hyper")
CLASSIFICADORES=("axgb" "incremental")


executar_testes() {
    for dataset in ${DATASETS[@]} 
    do
        for classificador in ${CLASSIFICADORES[@]} 
        do
            for x in $(seq $QNT_X)
            do
                $COMANDO_PYTHON $ARQUIVO_PYTHON $classificador $dataset $1 $2 $x
            done
        done
    done
}

# Max depth
# for valor in 1 5 10 15
for valor in 1 5
do
    executar_testes "max_depth" $valor
done

# Learning rate
# for valor in "0.01" "0.05" "0.1" "0.5"
for valor in "0.01" "0.05"
do
    executar_testes "learning_rate" $valor
done

# Max window size
# for valor in 512 1024 2048 4096 8192
for valor in 512 1024
do
    executar_testes "max_window_size" $valor
done

# Ensemble size
# for valor in 5 10 25 50 100
# do
#     executar_testes "ensemble_size" $valor
# done