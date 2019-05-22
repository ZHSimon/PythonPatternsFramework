from abc import ABC, abstractmethod


class TGAbstractPublisher(ABC):
    @abstractmethod
    def discard_unheard_events(self):
        pass

    @abstractmethod
    def publish(self, event, subject=None):
        pass

    @abstractmethod
    def publish_change(self, event_id, old_value, new_value):
        pass
