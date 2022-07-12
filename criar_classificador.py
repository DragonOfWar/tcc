import argumentos
from adaptive_semiV2 import AdaptiveSemi
from adaptive_xgboost import AdaptiveXGBoostClassifier
from modelos_adaptados_para_sklearn import (
    AdaptiveRandomForestClassifierA,
    HoeffdingAdaptiveTreeClassifierA,
)
from skmultiflow.meta import LeveragingBaggingClassifier, OzaBaggingClassifier
from skmultiflow.lazy import SAMKNNClassifier
from skmultiflow.trees import HoeffdingTreeClassifier


def criar_classficiador(**kwargs):
    if argumentos.CLASSIFICADOR == "axgb":
        return AdaptiveXGBoostClassifier(**kwargs)
    elif argumentos.CLASSIFICADOR == "afxgb":
        return AdaptiveSemi(reset_on_model_switch=False, detect_drift=False, **kwargs)
    elif argumentos.CLASSIFICADOR == "afxgb_r":
        return AdaptiveSemi(reset_on_model_switch=True, detect_drift=False, **kwargs)
    elif argumentos.CLASSIFICADOR == "afxgb_adwin":
        return AdaptiveSemi(reset_on_model_switch=False, detect_drift=True, **kwargs)
    elif argumentos.CLASSIFICADOR == "afxgb_adwin_r":
        return AdaptiveSemi(reset_on_model_switch=True, detect_drift=True, **kwargs)
    elif argumentos.CLASSIFICADOR == "arf":
        return AdaptiveRandomForestClassifierA(**kwargs)
    elif argumentos.CLASSIFICADOR == "hat":
        return HoeffdingAdaptiveTreeClassifierA(**kwargs)
    elif argumentos.CLASSIFICADOR == "lbht":
        return LeveragingBaggingClassifier(
            base_estimator=HoeffdingTreeClassifier(), **kwargs
        )
    elif argumentos.CLASSIFICADOR == "obht":
        return OzaBaggingClassifier(base_estimator=HoeffdingTreeClassifier(), **kwargs)
    elif argumentos.CLASSIFICADOR == "samknn":
        return SAMKNNClassifier(**kwargs)
    raise Exception(f"{argumentos.CLASSIFICADOR} não está disponível")
