from abc import ABC, abstractmethod


class TGAbstractRepresentable(ABC):
    @abstractmethod
    def get_code(self):
        pass
