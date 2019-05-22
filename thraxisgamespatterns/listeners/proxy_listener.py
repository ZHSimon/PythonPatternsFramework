from thraxisgamespatterns.listeners.abstract_listener import TGAbstractListener
from thraxisgamespatterns.listeners.dummy_listener import TGDummyListener


class TGListenerProxy(TGAbstractListener):
    def __init__(self, listener=None, event_id=None):
        super().__init__(event_id)
        self.listener = TGDummyListener(event_id) if (event_id and not listener) else listener

    def get_event_id(self):
        return self.listener.get_event_id()

    def on_event(self, event=None):
        self.listener.on_event(event)

    def set_listener(self, listener):
        if not listener.get_event_id() == self.listener.get_event_id():
            self.listener = listener
