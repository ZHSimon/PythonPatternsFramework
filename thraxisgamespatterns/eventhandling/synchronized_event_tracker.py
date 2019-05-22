from thraxisgamespatterns.eventhandling.abstract_event_tracker import TGAbstractEventTracker


class TGSynchronizedEventTracker(TGAbstractEventTracker):
    def __init__(self):
        self.events = []

    def forget_pending(self, event_id):
        self.events.remove(event_id)

    def is_pending(self, event_id):
        return self.events.__contains__(event_id)

    def track_pending_event(self, event_id):
        self.events.append(event_id)
