from abc import abstractmethod

from thraxisgamespatterns.rules.abstract_applicable import TGAbstractApplicable


class TGAbstractRule(TGAbstractApplicable):
    @abstractmethod
    def is_applicable(self, context):
        pass

    @abstractmethod
    def apply_to(self, context):
        pass

    def consider_applying(self, context):
        if self.is_applicable(context):
            self.apply_to(context)
