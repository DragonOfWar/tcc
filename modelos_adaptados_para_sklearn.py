# Esses modelos foram adaptados para que tenham compatibilidade com GridSearchCV do sklearn.
# Sem essas adaptações, o GridSearchCV dará erro

from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier
from skmultiflow.meta import AdaptiveRandomForestClassifier


class HoeffdingAdaptiveTreeClassifierA(HoeffdingAdaptiveTreeClassifier):
    def _more_tags(self):
        return {"pairwise": False}


class AdaptiveRandomForestClassifierA(AdaptiveRandomForestClassifier):
    def _more_tags(self):
        return {"pairwise": False}
