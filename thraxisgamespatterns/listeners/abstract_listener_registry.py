from abc import ABC, abstractmethod


class TGAbstractListenerRegistry(ABC):
    @abstractmethod
    def unregister_interest(self, listeners):
        pass

    @abstractmethod
    def register_interest(self, listener):
        pass
