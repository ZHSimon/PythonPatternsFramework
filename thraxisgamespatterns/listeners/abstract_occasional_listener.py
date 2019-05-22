from abc import abstractmethod

from thraxisgamespatterns.listeners.abstract_listener import TGAbstractListener


class TGAbstractOccasionalListener(TGAbstractListener):
    @abstractmethod
    def is_interested(self, event):
        pass

    @abstractmethod
    def on_interested_event(self, event):
        pass

    def on_event(self, event=None):
        if self.is_interested(event):
            self.on_interested_event(event)
