from thraxisgamespatterns.listeners.abstract_listener import TGAbstractListener


class TGDummyListener(TGAbstractListener):

    def on_event(self, event=None):
        pass  # Ignore the event.
