from abc import abstractmethod

from thraxisgamespatterns.rules.abstract_rule import TGAbstractRule


class TGAbstractDoNothingRule(TGAbstractRule):
    @abstractmethod
    def is_applicable(self, context):
        pass

    def apply_to(self, context):
        pass  # Do nothing
