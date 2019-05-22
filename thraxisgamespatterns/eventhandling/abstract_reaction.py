from abc import ABC, abstractmethod


class TGAbstractReaction(ABC):
    @abstractmethod
    def react_to(self, subject):
        pass
