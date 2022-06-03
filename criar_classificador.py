import argumentos
from adaptive_semiV2 import AdaptiveSemi
from adaptive_xgboost import AdaptiveXGBoostClassifier
from modelos_adaptados_para_sklearn import (
    AdaptiveRandomForestClassifierA,
    HoeffdingAdaptiveTreeClassifierA,
)


def criar_classficiador(**kwargs):
    if argumentos.CLASSIFICADOR == "axgb":
        return AdaptiveXGBoostClassifier(**kwargs)
    elif argumentos.CLASSIFICADOR == "gustavo":
        return AdaptiveSemi(reset_on_model_switch=False, detect_drift=False, **kwargs)
    elif argumentos.CLASSIFICADOR == "gustavo_r":
        return AdaptiveSemi(reset_on_model_switch=True, detect_drift=False, **kwargs)
    elif argumentos.CLASSIFICADOR == "gustavo_adwin":
        return AdaptiveSemi(reset_on_model_switch=False, detect_drift=True, **kwargs)
    elif argumentos.CLASSIFICADOR == "gustavo_adwin_r":
        return AdaptiveSemi(reset_on_model_switch=True, detect_drift=True, **kwargs)
    elif argumentos.CLASSIFICADOR == "arf":
        return AdaptiveRandomForestClassifierA(**kwargs)
    elif argumentos.CLASSIFICADOR == "hat":
        return HoeffdingAdaptiveTreeClassifierA(**kwargs)
    raise Exception(f"{argumentos.CLASSIFICADOR} não está disponível")
