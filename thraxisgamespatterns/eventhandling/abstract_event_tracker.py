from abc import ABC, abstractmethod


class TGAbstractEventTracker(ABC):
    @abstractmethod
    def forget_pending(self, event_id):
        pass

    @abstractmethod
    def is_pending(self, event_id):
        pass

    @abstractmethod
    def track_pending_event(self, event_id):
        pass
