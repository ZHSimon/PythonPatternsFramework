from abc import abstractmethod

from thraxisgamespatterns.listeners.abstract_listener import TGAbstractListener


class TGAbstractEventSubjectListener(TGAbstractListener):
    def on_event(self, event=None):
        self.on_event_handle(event.get_subject())

    @abstractmethod
    def on_event_handle(self, subject):
        pass
