from abc import abstractmethod

from thraxisgamespatterns.rules.abstract_rule import TGAbstractRule


class TGAbstractOtherwiseRule(TGAbstractRule):

    @abstractmethod
    def apply_to(self, context):
        pass

    @abstractmethod
    def is_applicable(self, context):
        return True
