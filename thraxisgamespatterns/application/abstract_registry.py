import logging
from abc import ABC

from thraxisgamespatterns.application.handler_map_factory import TGHandlerMapFactory
from thraxisgamespatterns.eventhandling.event_distributor import TGEventDistributor
from thraxisgamespatterns.factories.logging_rule_engine_factory import TGLoggingRuleEngineFactory


class TGAbstractRegistry(ABC):
    def __init__(self):
        self.rule_engine = TGLoggingRuleEngineFactory().create()
        self.logger = logging.getLogger()
        self.event_distributor = TGEventDistributor(logging.getLogger())
        self.handler_map_factory = TGHandlerMapFactory().create()
