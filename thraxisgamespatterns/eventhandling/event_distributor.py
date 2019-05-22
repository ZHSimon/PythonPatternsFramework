from collections import OrderedDict

from thraxisgamespatterns.eventhandling.abstract_publisher import TGAbstractPublisher
from thraxisgamespatterns.eventhandling.event import TGEvent
from thraxisgamespatterns.eventhandling.value_change import TGValueChange
from thraxisgamespatterns.listeners.abstract_listener_registry import TGAbstractListenerRegistry

MAX_UNHEARD_EVENTS = 10
UNPUBLISHED = "UNPUBLISHED"


class TGEventDistributor(TGAbstractPublisher, TGAbstractListenerRegistry):
    def __init__(self, logger):
        self.logger = logger
        self.listener_map = {UNPUBLISHED: []}
        self.unheard_events = OrderedDict()

    def check_unheard_events(self, listener):
        event = self.unheard_events.pop(listener.get_event_id())
        if event:
            self.distribute(event, listener)

    def consider_removing(self, event_id, listeners):
        if not listeners:
            self.listener_map.pop(event_id, None)

    def create_change_event(self, event_id, old_value, new_value):
        change = TGValueChange(event_id, old_value, new_value)
        return TGEvent(change.event_id, change)

    def unregister_interest(self, listeners):
        if type(listeners) is not list:
            listeners = [listeners]
        for listener in listeners:
            if listener.get_event_id() in self.listener_map:
                listeners = self.listener_map.get(listener.get_event_id())
                listeners.remove(listener)
                self.consider_removing(listener.get_event_id(), listeners)

    def discard_unheard_events(self):
        self.unheard_events.clear()

    def distribute(self, event, listener):
        listener.on_event(event)

    def distribute_event(self, event, listeners=None):
        if not listeners or type(listeners) is not list:
            listeners = self.listener_map.get(event.get_id())
        if listeners:
            original_listeners = listeners
            for listener in original_listeners:
                self.distribute(event, listener)
        else:
            self.handle_no_listeners(event)

    def handle_no_listeners(self, event):
        self.make_room_for_unheard_event()
        self.unheard_events.update({event.get_id(): event})

    def make_room_for_unheard_event(self):
        if len(self.unheard_events) >= MAX_UNHEARD_EVENTS:
            self.unheard_events.popitem()

    def publish(self, event, subject=None):
        self.distribute_event(event)

    def publish_change(self, event_id, old_value, new_value):
        if event_id and old_value and new_value and not (old_value == new_value):
            self.distribute_event(self.create_change_event(event_id, old_value, new_value))

    def register_interest(self, listener):
        if listener.get_event_id() and not self.listener_map.__contains__(listener.get_event_id()):
            self.listener_map.update({listener.get_event_id(): []})
        listener_list = self.listener_map.get(listener.get_event_id())
        listener_list.append(listener)
        self.check_unheard_events(listener)
