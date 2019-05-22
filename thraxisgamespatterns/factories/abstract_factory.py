from abc import ABC, abstractmethod


class TGAbstractFactory(ABC):
    @abstractmethod
    def create(self, options=None):
        pass
