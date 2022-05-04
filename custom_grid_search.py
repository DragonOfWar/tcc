from statistics import mean
from sklearn.metrics import accuracy_score
from typing import Any

from sklearn.model_selection import KFold

ParamGrid = dict[str, list[Any]]
Params = dict[str, Any]
ParamCombs = list[Params]


class CustomGridSearch:
    def __init__(self, param_grid: ParamGrid) -> None:
        self.combinacoes_parametros = self._gerar_combinacoes(param_grid)
        self.best = {}

    def _gerar_combinacoes(self, dic: ParamGrid, data: Params = {}) -> ParamCombs:
        chave = None
        chaves_data = list(data.keys())
        for c in dic.keys():
            if c not in chaves_data:
                chave = c
                break
        else:
            return [data]
        resultado: ParamCombs = []
        for valor in dic[chave]:
            copy = data.copy()
            copy[chave] = valor
            resultado += self._gerar_combinacoes(dic, copy)
        return resultado

    def exec_train(self, X_train, y_train, X_test, y_test, func_criar_modelo, params):
        modelo = func_criar_modelo(**params)
        modelo.fit(X_train, y_train)
        return accuracy_score(X_test, modelo.predict(X_test))

    def exec(self, X, y, func_criar_modelo) -> Params:
        for i, params in enumerate(self.combinacoes_parametros):
            print(f"({i+1}/{len(self.combinacoes_parametros)})")
            kf = KFold(n_splits=5)
            acuracias = []
            for traini, testi in kf.split(X):
                modelo = func_criar_modelo(**params)
                modelo.fit(X[traini], y[traini])
                acuracias.append(accuracy_score(y[testi], modelo.predict(X[testi])))
            params["acuracia"] = mean(acuracias)
        best = min(self.combinacoes_parametros, key=lambda x: x["acuracia"])
        return best
