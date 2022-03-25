from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier
from skmultiflow.meta import AdaptiveRandomForestClassifier


class HoeffdingAdaptiveTreeClassifierA(HoeffdingAdaptiveTreeClassifier):
    def _more_tags(self):
        return {"pairwise": False}


class AdaptiveRandomForestClassifierA(AdaptiveRandomForestClassifier):
    def _more_tags(self):
        return {"pairwise": False}
