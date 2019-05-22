from abc import ABC, abstractmethod


class TGAbstractMatcher(ABC):
    @abstractmethod
    def is_match(self, element):
        pass
