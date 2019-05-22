from abc import abstractmethod

from thraxisgamespatterns.rules.abstract_applicable import TGAbstractApplicable


class TGAbstractStatefulRule(TGAbstractApplicable):

    def consider_applying(self):
        if self.is_applicable():
            self.apply()

    def apply_to(self, context=None):
        self.apply()

    @abstractmethod
    def apply(self):
        pass

    @abstractmethod
    def is_applicable(self, context):
        pass
