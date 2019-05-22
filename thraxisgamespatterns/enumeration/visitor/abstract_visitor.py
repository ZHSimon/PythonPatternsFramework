from abc import ABC, abstractmethod


class TGAbstractVisitor(ABC):

    @abstractmethod
    def visit_any(self):
        pass


NOTHING = None
