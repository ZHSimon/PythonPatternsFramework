# package com.games.thraxis.framework.eventhandling.eventmonitoring;
#
# import java.util.Collection;
#
# import com.games.thraxis.framework.enumeration.enumerator.TGBasicEnumerator;
# import com.games.thraxis.framework.enumeration.enumerator.TGEnumerator;
# import com.games.thraxis.framework.enumeration.matcher.TGMatcher;
# import com.games.thraxis.framework.listeners.TGListener;
#
# /##
#  # Created by Zack on 9/26/2017.
#  #/
#
# public abstract class TGBaseEventMonitor implements TGEventMonitor {
#
# 	private final TGEnumerator enumerator = TGBasicEnumerator.DEFAULT;
#
# 	protected <I, C extends Collection<? extends I>> boolean anySatisfy(C items, TGMatcher<I> matcher) {
# 		return enumerator.anySatisfy(items, matcher);
# 	}
#
# 	public boolean areEventsPending(Collection<TGListener<?>> listeners) {
# 		return anySatisfy(listeners, new TGMatcher<TGListener<?>>() {
# 			@Override
# 			public boolean isMatch(TGListener<?> listener) {
# 				return isPending(listener.getEventId());
# 			}
# 		});
# 	}
#
# 	public boolean isListeningTo(Collection<TGListener<?>> listeners, final String eventId) {
# 		return anySatisfy(listeners, new TGMatcher<TGListener<?>>() {
# 			@Override
# 			public boolean isMatch(TGListener<?> listener) {
# 				return listener.getEventId().equals(eventId);
# 			}
# 		});
# 	}
#
# 	@Override
# 	public boolean isWaitingFor(String eventId) {
# 		return isPending(eventId) && isListeningTo(eventId);
# 	}
#
# }
from eventhandling.eventmonitoring.abstract_event_monitor import TGAbstractEventMonitor
from enumeration.matcher.abstract_matcher import TGAbstractMatcher
from enumeration.enumerator.basic_enumerator import TGBasicEnumerator
from abc import ABC


# class EventsPendingMatcher(TGAbstractMatcher):
#     def __init__(self, event_monitor):
#         self.event_monitor = event_monitor
#
#     def is_match(self, listener):
#         return self.event_monitor.is_pending(listener.get_event_id())


def events_pending_is_match(self, listener):
    return self.event_monitor.is_pending(listener.get_event_id())

# class IsListeningToMatcher(TGAbstractMatcher):
#     def __init__(self, event_id):
#         self.event_id = event_id
#
#     def is_match(self, listener):
#         return listener.get_event_id() == self.event_id


def listening_is_match(self, listener):
    return listener.get_event_id() == self.event_id


class TGAbstractBaseEventMonitor(ABC, TGAbstractEventMonitor):

    def are_events_pending(self, listeners):
        # return self.any_satisfy(listeners, EventsPendingMatcher(self))
        return self.any_satisfy(listeners, type('EventsPendingMatcher', (TGAbstractMatcher,),
                                                dict(event_monitor=self,
                                                     is_match=events_pending_is_match)))

    def is_listening_to(self, listeners, event_id):
        # return self.any_satisfy(listeners, IsListeningToMatcher(event_id))
        return self.any_satisfy(listeners, type('IsListeningToMatcher', (TGAbstractMatcher,),
                                                dict(event_id=event_id,
                                                     is_match=listening_is_match)))

    @staticmethod
    def any_satisfy(items, matcher):
        return DEFAULT.any_satisfy(items, matcher)

    def is_waiting_for(self, event_id):
        return self.is_pending(event_id) and self.is_listening_to(event_id)


DEFAULT = TGBasicEnumerator()
