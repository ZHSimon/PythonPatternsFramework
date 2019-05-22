from abc import abstractmethod

from thraxisgamespatterns.listeners.abstract_listener import TGAbstractListener


class TGAbstractEventSubjectUnusedListener(TGAbstractListener):
    @abstractmethod
    def on_event(self, event=None):
        pass
