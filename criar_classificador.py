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


AFXGB_CONIFGS = [
    "afxgb",
    "afxgb_r",
    "afxgb_adwin",
    "afxgb_adwin_r_update100",
    "afxgb_adwin_r_update75",
    "afxgb_adwin_r_update50",
    "afxgb_adwin_r_update25",
    "afxgb_adwin_r_update0",
]


def criar_classficiador(**kwargs):
    if argumentos.CLASSIFICADOR == "axgb":
        return AdaptiveXGBoostClassifier(**kwargs)
    elif argumentos.CLASSIFICADOR in AFXGB_CONIFGS:
        return AdaptiveSemi(**kwargs)
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
