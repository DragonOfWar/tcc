import argumentos
import salvar_resultados
from criar_classificador import criar_classficiador
from skmultiflow.data import AGRAWALGenerator
from sklearn.model_selection import GridSearchCV


parameter_grid = {}
if argumentos.CLASSIFICADOR == "axgb":
    parameter_grid = {
        "max_depth": [1, 5, 10, 15],
        "learning_rate": [0.01, 0.05, 0.1, 0.5],
        "max_window_size": [512, 1024, 2048, 4096, 8192],
        "min_window_size": [4, 8, 16],
    }
elif argumentos.CLASSIFICADOR == "incremental":
    parameter_grid = {
        "max_window_size": [512, 1000, 2048, 4096],
        "min_window_size": [1, 4, 8, 16],
        "pre_train": [15, 60, 120, 300],
        "max_buffer": [25, 100, 200, 500],
        "max_depth": [1, 6, 10, 15],
        "learning_rate": [0.05, 0.1, 0.3, 0.5],
    }
elif argumentos.CLASSIFICADOR == "arf":
    parameter_grid = {"n_estimators": [5, 10, 20, 30]}

print(f"Carregando dataset {argumentos.DATASET}")
dataset = AGRAWALGenerator(random_state=1).next_sample(argumentos.MAX_REGISTROS)
print(f"Realizando GridSearchCV")

gs_cv = GridSearchCV(criar_classficiador(), parameter_grid)
gs_cv.fit(dataset[0], dataset[1])

print("Salvando resultados")
salvar_resultados.salvar_resultados_gridsearch(gs_cv.cv_results_, gs_cv.best_params_)
