from abc import ABC, abstractmethod


class TGAbstractListener(ABC):
    def __init__(self, event_id):
        self.event_id = event_id

    def get_event_id(self):
        return self.event_id

    @abstractmethod
    def on_event(self, event=None):
        pass
