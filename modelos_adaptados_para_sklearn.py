# Esses modelos foram adaptados para que tenham compatibilidade com GridSearchCV do sklearn.
# Sem essas adaptações, o GridSearchCV dará erro

from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier
from skmultiflow.meta import AdaptiveRandomForestClassifier


class HoeffdingAdaptiveTreeClassifierA(HoeffdingAdaptiveTreeClassifier):
    # Resolve um erro que ocorre com o stagger_g
    def _new_learning_node(
        self, initial_class_observations=None, is_active=True, is_active_node=True
    ):
        return super()._new_learning_node(initial_class_observations)

    def _more_tags(self):
        return {"pairwise": False}


class AdaptiveRandomForestClassifierA(AdaptiveRandomForestClassifier):
    def _more_tags(self):
        return {"pairwise": False}
