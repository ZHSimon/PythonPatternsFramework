from abc import abstractmethod

from thraxisgamespatterns.enumeration.enumerator.basic_enumerator import TGBasicEnumerator
from thraxisgamespatterns.enumeration.matcher.abstract_matcher import TGAbstractMatcher
from thraxisgamespatterns.eventhandling.eventmonitoring.abstract_event_monitor import TGAbstractEventMonitor


def events_pending_is_match(self, listener):
    return self.event_monitor.is_pending(listener.get_event_id())


def listening_is_match(self, listener):
    return listener.get_event_id() == self.event_id


class TGAbstractBaseEventMonitor(TGAbstractEventMonitor):

    @abstractmethod
    def check_pending_event(self, event_id):
        pass

    @abstractmethod
    def check_pending_events(self):
        pass

    @abstractmethod
    def is_pending(self, event_id):
        pass

    @abstractmethod
    def register_listener(self, listener):
        pass

    @abstractmethod
    def unregister_listeners(self, listeners=None):
        pass

    def are_events_pending(self, listeners=None):
        # return self.any_satisfy(listeners, EventsPendingMatcher(self))
        return self.any_satisfy(listeners, type('EventsPendingMatcher', (TGAbstractMatcher,),
                                                {'event_monitor': self,
                                                 'is_match': events_pending_is_match}))

    def is_listening_to(self, event_id, listeners=None):
        # return self.any_satisfy(listeners, IsListeningToMatcher(event_id))
        return self.any_satisfy(listeners, type('IsListeningToMatcher', (TGAbstractMatcher,),
                                                {'event_id': event_id,
                                                 'is_match': listening_is_match}))

    @staticmethod
    def any_satisfy(items, matcher):
        return DEFAULT.any_satisfy(items, matcher)

    def is_waiting_for(self, event_id):
        return self.is_pending(event_id) and self.is_listening_to(event_id)


DEFAULT = TGBasicEnumerator()
