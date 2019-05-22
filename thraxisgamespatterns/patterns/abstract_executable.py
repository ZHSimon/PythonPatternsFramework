from abc import ABC, abstractmethod


class TGAbstractExecutable(ABC):

    @abstractmethod
    def execute(self):
        pass
