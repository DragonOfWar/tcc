#!/bin/bash

COMANDO_PYTHON="python3"
ARQUIVO_TESTES="adaptive_xgboost_example.py"
CODIGO_GERAR_GRAFICOS="gerar_graficos.py"
ARQUIVO_GRIDSEARCH="grid_cv.py"
MAX_REGISTROS=500000
QNT_X=$($COMANDO_PYTHON config.py qnt_x)
DATASETS=$($COMANDO_PYTHON config.py datasets)
DATASET_GS=$($COMANDO_PYTHON config.py dataset_gridsearch)
CLASSIFICADORES=$($COMANDO_PYTHON config.py classificadores)
QNT_DRIFTS=9

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
    echo "CLASSIFICADOR: $classificador"
    if [ "$EXECUTAR_GS" = true ]
    then
        echo "  Executando GridSearch"
        COMANDO="$COMANDO_PYTHON $ARQUIVO_GRIDSEARCH --classificador=$classificador --dataset=$DATASET_GS --maxregistros=$MAX_REGISTROS --qntdrifts=0"
        echo "  Comando: $COMANDO"
        $COMANDO 2> logs/err_gs_$classificador.log
    fi
    for dataset in ${DATASETS[@]}
    do
        for x in $(seq $QNT_X)
        do
            echo "  Experimento usando $dataset ($x/$QNT_X)."
            COMANDO="$COMANDO_PYTHON $ARQUIVO_TESTES --classificador=$classificador --dataset=$dataset --iteracao=$x --maxregistros=$MAX_REGISTROS --randomstate=$x --qntdrifts=$QNT_DRIFTS"
            echo "  Comando: $COMANDO"
            $COMANDO 2> logs/err_"$classificador"_"$dataset"_"$x".log
        done
    done
done

$COMANDO_PYTHON $CODIGO_GERAR_GRAFICOS --friedmantotal