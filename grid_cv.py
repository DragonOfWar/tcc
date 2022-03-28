import argumentos
import numpy as np
import salvar_resultados

from adaptive_xgboost import AdaptiveXGBoostClassifier
from adaptive_semiV2 import AdaptiveSemi
from modelos_adaptados_para_sklearn import (
    AdaptiveRandomForestClassifierA,
    HoeffdingAdaptiveTreeClassifierA,
)
from sklearn.model_selection import train_test_split, GridSearchCV


def _criar_modelo(**kwargs):
    if argumentos.CLASSIFICADOR == "axgb":
        return AdaptiveXGBoostClassifier(**kwargs)
    elif argumentos.CLASSIFICADOR == "incremental":
        return AdaptiveSemi(
            max_buffer=25,
            pre_train=15,
            **kwargs,
        )
    elif argumentos.CLASSIFICADOR == "arf":
        return AdaptiveRandomForestClassifierA(**kwargs)
    elif argumentos.CLASSIFICADOR == "hat":
        return HoeffdingAdaptiveTreeClassifierA(**kwargs)


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
        "max_depth": [1, 5, 10, 15],
        "learning_rate": [0.01, 0.05, 0.1, 0.5],
        "max_window_size": [512, 1024, 2048, 4096, 8192],
        "min_window_size": [4, 8, 16],
        "reset_on_model_switch": [True, False],
    }
elif argumentos.CLASSIFICADOR == "arf":
    parameter_grid = {"n_estimators": [5, 10, 20, 30]}

print(f"Carregando dataset {argumentos.DATASET}")
dataset = np.loadtxt(f"datasets/{argumentos.DATASET}.csv", delimiter=",", skiprows=1)
print(f"Configurando dataset")
X, y = dataset[:, :-1], dataset[:, -1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.3, random_state=1
)
gs_cv = GridSearchCV(_criar_modelo(), parameter_grid)
print(f"Realizando GridSearchCV")
gs_cv.fit(X_train, y_train)

print("Salvando resultados")
salvar_resultados.salvar_resultados_gridsearch(gs_cv.cv_results_, gs_cv.best_params_)

# CUSTOM GRID SEARCH
# Grid search CV
# def grid_search_cross_val(param_grid, X_train, y_train, param_i=0, params={}):
#     param = list(param_grid.keys())[param_i]
#     cross_val_scores = []
#     for value in param_grid[param]:
#         print(f"{param}: {value}")
#         params[param] = value
#         if param_i < len(param_grid) - 1:
#             cross_val_scores += grid_search_cross_val(
#                 param_grid, X_train, y_train, param_i + 1, params
#             )
#         else:
#             model = _criar_modelo(**params)
#             scores = cross_val_score(model, X_train, y_train, cv=10, scoring="accuracy")
#             score = params.copy()
#             score["score"] = np.mean(scores)
#             cross_val_scores.append(score)
#     return cross_val_scores


# res = grid_search_cross_val(parameter_grid, X_train, y_train)
# print("aqui")
