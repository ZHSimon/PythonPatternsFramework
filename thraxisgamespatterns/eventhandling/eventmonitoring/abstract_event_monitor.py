from abc import ABC, abstractmethod


class TGAbstractEventMonitor(ABC):
    @abstractmethod
    def are_events_pending(self, listeners=None):
        pass

    @abstractmethod
    def check_pending_event(self, event_id):
        pass

    @abstractmethod
    def check_pending_events(self):
        pass

    @abstractmethod
    def is_listening_to(self, event_id, listeners=None):
        pass

    @abstractmethod
    def is_pending(self, event_id):
        pass

    @abstractmethod
    def is_waiting_for(self, event_id):
        pass

    @abstractmethod
    def register_listener(self, listener):
        pass

    @abstractmethod
    def unregister_listeners(self, listeners=None):
        pass
