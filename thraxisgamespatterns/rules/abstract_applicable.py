from abc import ABC, abstractmethod


class TGAbstractApplicable(ABC):

    @abstractmethod
    def is_applicable(self, context):
        pass

    @abstractmethod
    def apply_to(self, context):
        pass
