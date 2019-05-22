from thraxisgamespatterns.eventhandling.eventmonitoring.abstract_base_event_monitor import TGAbstractBaseEventMonitor


class TGBasicEventMonitor(TGAbstractBaseEventMonitor):
    def __init__(self, registry):
        self.event_tracker = registry.get_event_tracker()
        self.listener_registry = registry.get_listener_registry()
        self.listeners = []

    def are_events_pending(self, listeners=None):
        return super().are_events_pending(self.listeners)

    def check_pending_event(self, event_id):
        return  # Do nothing - decorators will override as needed.

    def check_pending_events(self):
        return  # Do nothing - decorators will override as needed.

    def is_listening_to(self, event_id, listeners=None):
        return super().is_listening_to(self.listeners, event_id)

    def is_pending(self, event_id):
        return self.event_tracker.is_pending(event_id)

    def register_listener(self, listener):
        self.listeners.append(listener)
        self.listener_registry.register_interest(listener)

    def unregister_listeners(self, listeners=None):
        self.listener_registry.unregister_interest(listeners)
        listeners.clear()
