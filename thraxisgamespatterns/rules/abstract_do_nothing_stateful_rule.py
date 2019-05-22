from abc import abstractmethod

from thraxisgamespatterns.rules.abstract_stateful_rule import TGAbstractStatefulRule


class TGAbstractDoNothingStatefulRule(TGAbstractStatefulRule):

    @abstractmethod
    def is_applicable(self, context):
        pass

    def apply(self):
        pass  # Do nothing.
